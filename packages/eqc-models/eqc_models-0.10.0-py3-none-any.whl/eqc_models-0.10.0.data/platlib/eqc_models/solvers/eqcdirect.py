# (C) Quantum Computing Inc., 2024.
from typing import Dict
import logging
import numpy as np
from eqc_direct.client import EqcClient
from eqc_models.base.base import ModelSolver, EqcModel

log = logging.getLogger(name=__name__)


class EqcDirectMixin:
    """
    This class provides an instance method and property that
    manage the direct connection to a QCi device.

    """

    ip_addr = None
    port = None

    def connect(self, ip_addr: str, port: str) -> str:
        """
        Explicitly set device address; if environment is
        configured with the connection, this call is not required.

        Parameters
        ------------

        ip_addr: The IP address of the device.

        port: The port number of the device.

        Parameters
        ------------
        The status.

        """
        self.ip_addr = ip_addr
        self.port = port
        client = self.client
        return client.system_status()["status_desc"]

    @property
    def client(self):
        params = {}
        if self.ip_addr is not None:
            params["ip_address"] = self.ip_addr
        if self.port is not None:
            params["port"] = self.port
        return EqcClient(**params)


class EqcDirectSolver(ModelSolver, EqcDirectMixin):
    """
    This class provides an instance method for direct submission
    of jobs to QCi devices.

    """

    def solve(
        self,
        model: EqcModel,
        relaxation_schedule: int = 2,
        precision: float = 1.0,
    ) -> Dict:
        """Parameters
        -------------
        model: An EqcModel instance.

        relaxation_schedule: A predefined schedule indicator which
        sets parameters on the device to control the sampling through
        photon measurement; default is 2.

        precision: A value which, when not None, indicates
        the numerical precision desired in the solution: 1 for
        integer, 0.1 for tenths place, 0.01 for hundreths and None for
        raw; default is 1.0.

        Returns
        ---------
        Json response from the solver.

        """
        poly_coefficients, poly_indices = model.sparse
        # print(poly_indices)
        if model.machine_slacks > 0:
            # add a single 0 coefficient entry as the next-highest index
            highest_idx = int(np.max(poly_indices))
            # print("POLY HIGHEST", highest_idx)
            for i in range(model.machine_slacks):
                addtl_index = [0 for i in range(len(poly_indices[0]))]
                addtl_index[-1] = highest_idx + i + 1
                poly_indices = poly_indices.tolist() + [addtl_index]
                poly_coefficients = poly_coefficients.tolist() + [0]
        # print(poly_indices)
        scval = model.sum_constraint

        client = self.client
        lock_id, start_ts, end_ts = client.wait_for_lock()
        log.debug(
            "Got device lock id %s. Wait time %f",
            lock_id,
            end_ts - start_ts,
        )
        resp = None
        try:
            log.debug(
                "Calling device with parameters relaxation_schedule %d sum_constraint %s lock_id %s solution_precision %f",
                relaxation_schedule,
                scval,
                lock_id,
                precision,
            )
            resp = client.process_job(
                poly_coefficients=poly_coefficients,
                poly_indices=poly_indices,
                relaxation_schedule=relaxation_schedule,
                sum_constraint=scval,
                lock_id=lock_id,
                solution_precision=precision,
            )
            log.debug("Received response with status %s", resp["err_desc"])
            log.debug(
                "Runtime %f resulting in energy %f",
                resp["runtime"],
                resp["energy"],
            )
            log.debug(
                "Distillation runtime %s resulting in energy %f",
                resp["distilled_runtime"],
                resp["distilled_energy"],
            )
        finally:
            client.release_lock(lock_id=lock_id)
        if resp is not None:
            solution = resp["solution"]
            energy = resp["energy"]
            runtime = resp["runtime"]
            dirac3_sol = np.array(solution)
            log.debug(
                "Energy %f Runtime %f Solution Size %i Solution Sum %f",
                energy,
                runtime,
                len(dirac3_sol),
                sum(dirac3_sol),
            )
        else:
            raise RuntimeError("FAILED TO GET RESPONSE")
        return resp


class Dirac3DirectSolver(EqcDirectSolver):

    """
    Naming this for when when other devices are available and have
    different requirements. For instance, Dirac-3 requires the
    summation constraint parameter, but others might not. The same
    could be true for relaxation schedule.

    """
