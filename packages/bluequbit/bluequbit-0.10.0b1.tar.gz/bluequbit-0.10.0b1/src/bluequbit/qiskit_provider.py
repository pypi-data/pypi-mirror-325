from __future__ import annotations

import warnings
from collections import defaultdict
from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives.backend_sampler_v2 import Options as BackendSamplerV2Options
from qiskit.primitives.base import BaseEstimatorV2, BaseSamplerV2
from qiskit.primitives.containers import (
    DataBin,
    PrimitiveResult,
    PubResult,
    SamplerPubLike,
    SamplerPubResult,
)
from qiskit.primitives.containers.estimator_pub import EstimatorPub
from qiskit.primitives.containers.sampler_pub import SamplerPub
from qiskit.primitives.primitive_job import PrimitiveJob
from qiskit.quantum_info import Statevector
from qiskit.result import Result
from qiskit.result.models import ExperimentResult, ExperimentResultData

import bluequbit

from . import job_metadata_constants

if TYPE_CHECKING:
    from collections.abc import Iterable

    from qiskit.primitives.containers import EstimatorPubLike
    from qiskit.providers.backend import BackendV2

    from .job_result import JobResult


def _to_bq_qiskit_job(primitive, jobs, backend):
    if not isinstance(jobs, list):
        # Only 1 job
        jobs = [jobs]
    return [BlueQubitQiskitJob(primitive, "local", backend, job) for job in jobs]


@dataclass
class BQDataBin:
    meas: Result


class BlueQubitQiskitJob:
    def __init__(
        self, primitive: str, job_id: str, backend: BlueQubitBackend, job: JobResult
    ):
        super().__init__()
        self.primitive = primitive
        self.job_id = job_id
        self.backend = backend
        self.job = job

    @property
    def data(self):
        pub_results: list[PrimitiveResult] = []

        finished = self.job
        if self.backend.execution_mode != "local":
            finished = self.backend.bq_client.wait(self.job.job_id)  # type: ignore[assignment]

        if self.primitive == "estimator":
            evs = finished.expectation_value
            pub_result = PubResult(DataBin(evs=evs))
        else:
            if self.primitive != "sampler":
                raise Exception(f"Unexpected primitive {self.primitive}")
            pub_result = PubResult(BQDataBin(finished))

        pub_results.append(pub_result)
        # For now
        assert len(pub_results) == 1
        return pub_results[0].data
        # TODO support multiple circuits
        # return PrimitiveResult(pub_results)

    def result(self):
        experiment_results: list[ExperimentResult] = []

        finished = self.job
        if self.backend.execution_mode != "local":
            finished = self.backend.bq_client.wait(self.job.job_id)  # type: ignore[assignment]

        sv = (
            Statevector(finished.get_statevector()).data
            if self.job.num_qubits <= job_metadata_constants.MAX_QUBITS_WITH_STATEVEC
            else None
        )

        data = ExperimentResultData(
            counts=finished.get_counts(),
            statevector=sv,
        )
        experiment_results.append(
            ExperimentResult(
                shots=self.job.shots,
                success=True,
                status=self.job.run_status,
                data=data,
            )
        )
        return Result(
            backend_name=f"bluequbit_{self.job.device}",
            backend_version=bluequbit.__version__,
            job_id=self.job.job_id,
            qobj_id=0,
            # TODO this is too restricted
            success=self.job.run_status == "COMPLETED",
            results=experiment_results,
            status=self.job.run_status,
        )


class BlueQubitBackend:
    def __init__(
        self,
        api_token: str | None = None,
        execution_mode="cloud",
        device="cpu",
    ):
        super().__init__()
        self.bq_client = bluequbit.init(
            api_token=api_token, execution_mode=execution_mode
        )
        self.device = device
        self.execution_mode = execution_mode

    def _run(
        self, run_input: QuantumCircuit | list[QuantumCircuit], shots: int | None = None
    ):
        jobs = self.bq_client.run(
            run_input, shots=shots, device=self.device, asynchronous=True
        )

        return _to_bq_qiskit_job("sampler", jobs, self)


class BlueQubitProvider:
    """A Qiskit provider for accessing BlueQubit backend.

    :param api_token: API token of the user. If ``None``, the token will be looked
                      in the environment variable BLUEQUBIT_API_TOKEN.
    """

    def __init__(self, api_token: str | None = None):
        super().__init__()
        self.api_token = api_token

    def get_backend(self, execution_mode: str | None = None, device: str = "cpu"):
        """
        :param execution_mode: Execution mode. Can be ``"cloud"``, ``"local"`` or ``None``.
                           If ``None``, the environment variable
                           BLUEQUBIT_EXECUTION_MODE will be used if set, otherwise
                           ``"cloud"`` will be used.
        :param device: device for which to run the circuit. Can be one of
                       ``"cpu"`` | ``"gpu"`` | ``"quantum"``
        """
        return BlueQubitBackend(
            api_token=self.api_token, execution_mode=execution_mode, device=device
        )


class EstimatorV2(BaseEstimatorV2):
    """
    Evaluates expectation values for provided quantum circuit and observable combinations.

    Qiskit Estimator V2 interface to BlueQubit cloud computation: https://docs.quantum.ibm.com/api/qiskit-ibm-runtime/qiskit_ibm_runtime.EstimatorV2
    Based on:
    - https://github.com/Qiskit/qiskit-ibm-runtime/blob/main/qiskit_ibm_runtime/estimator.py
    - https://github.com/Qiskit/qiskit-aer/blob/main/qiskit_aer/primitives/estimator_v2.py
    """

    def __init__(
        self,
        *,
        backend: BlueQubitBackend | None = None,
        options: dict | None = None,
    ):
        if options is None:
            options = {}
        self.options = options
        if backend is None:
            backend = BlueQubitBackend()
        self._backend = backend

    def run(
        self, pubs: Iterable[EstimatorPubLike], *, precision: float | None = None
    ) -> PrimitiveJob[PrimitiveResult[PubResult]]:
        if precision is not None:
            warnings.warn(
                "BlueQubit only supports float32 precision. The precision argument is going to be ignored.",
                UserWarning,
                stacklevel=2,
            )
        coerced_pubs = [EstimatorPub.coerce(pub, precision) for pub in pubs]
        job = PrimitiveJob(self._run, coerced_pubs)
        job._submit()  # noqa: SLF001
        return job

    def _run(self, pubs: list[EstimatorPub]) -> PrimitiveResult[PubResult]:
        return PrimitiveResult([self._run_pub(pub) for pub in pubs])

    def _run_pub(self, pub: EstimatorPub) -> PubResult:
        parameter_values = pub.parameter_values
        if parameter_values.num_parameters > 0:
            bound_circuits = parameter_values.bind_all(pub.circuit).tolist()
            assert isinstance(bound_circuits, QuantumCircuit), (
                "We do not support multiple params/obs in 1 PUB yet"
            )
            circuit = bound_circuits
        else:
            circuit = pub.circuit
        observables = pub.observables.tolist()
        if isinstance(observables, list):
            pauli_sums = [list(e.items()) for e in observables]
        else:
            # Only a single observable
            pauli_sums = list(observables.items())
        # Ignore this
        # precision = pub.precision
        jobs = self._backend.bq_client.run(
            circuit,
            device=self._backend.device,
            asynchronous=True,
            pauli_sum=pauli_sums,  # type: ignore[arg-type]
        )
        qiskit_jobs = _to_bq_qiskit_job("estimator", jobs, self._backend)
        if len(qiskit_jobs) != 1:
            raise Exception("Something is wrong TODO")
        return qiskit_jobs[0]


class SamplerV2(BaseSamplerV2):
    """
    Qiskit SamplerV2 interface to BlueQubit cloud computation.
    """

    def __init__(
        self,
        *,
        backend: BackendV2 | None = None,
        options: dict | None = None,
    ):
        """
        Args:
            backend: The backend to run the primitive on.
            options: The options to specify the BlueQubit device type.
                For now, if you specify ``seed_simulator`` for deterministic output,
                it will be ignored.
        """
        if options is not None and "seed_simulator" in options:
            warnings.warn(
                "BlueQubit doesn't support deterministic seed_simulator yet.",
                UserWarning,
                stacklevel=2,
            )

        if options is None:
            options = {}
        if backend is None:
            backend = BlueQubitBackend()

        self._backend = backend
        self._options = (
            BackendSamplerV2Options(**options) if options else BackendSamplerV2Options()
        )

    def run(
        self, pubs: Iterable[SamplerPubLike], *, shots: int | None = None
    ) -> PrimitiveJob[PrimitiveResult[SamplerPubResult]]:
        if shots is None:
            shots = self._options.default_shots
        coerced_pubs = [SamplerPub.coerce(pub, shots) for pub in pubs]
        job = PrimitiveJob(self._run, coerced_pubs)
        job._submit()  # noqa: SLF001
        return job

    def _run(self, pubs: list[SamplerPub]) -> PrimitiveResult[SamplerPubResult]:
        pub_dict = defaultdict(list)
        # consolidate pubs with the same number of shots
        for i, pub in enumerate(pubs):
            pub_dict[pub.shots].append(i)

        results = [None] * len(pubs)
        for shots, lst in pub_dict.items():
            # run pubs with the same number of shots at once
            pub_results = self._run_pubs([pubs[i] for i in lst], shots)
            # reconstruct the result of pubs
            for i, pub_result in zip(lst, pub_results):
                results[i] = pub_result
        return PrimitiveResult(results)

    def _run_pubs(self, pubs: list[SamplerPub], shots: int) -> list[SamplerPubResult]:
        """Compute results for pubs that all require the same value of ``shots``."""
        # prepare circuits
        bound_circuits = [pub.parameter_values.bind_all(pub.circuit) for pub in pubs]
        flatten_circuits: list[QuantumCircuit] = []
        for circuits in bound_circuits:
            flatten_circuits.extend(np.ravel(circuits).tolist())

        # run circuits
        results = self._backend._run(flatten_circuits, shots=shots)  # noqa: SLF001

        return results
