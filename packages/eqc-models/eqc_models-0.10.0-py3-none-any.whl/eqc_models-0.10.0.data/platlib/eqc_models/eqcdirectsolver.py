from typing import Dict
import logging
import numpy as np
from eqc_direct.client import EqcClient
from .base import ModelSolver

log = logging.getLogger(name=__name__)

class EqcDirectMixin:

    ip_addr = None
    port = None

    def connect(self, ip_addr : str, port : str):
        """ Explicitly set device address, if environment is configured with the connection, this call is not required """
        self.ip_addr = ip_addr
        self.port = port

    @property
    def client(self):
    
        params = {}
        if self.ip_addr is not None:
            params["ip_address"] = self.ip_addr
        if self.port is not None:
            params["port"] = self.port
        return EqcClient(**params)

class EqcDirectSolver(ModelSolver, EqcDirectMixin):

    def solve(self, relaxation_schedule:int=2, precision : float = 1.0) -> Dict:
        model = self.model
        poly_coefficients, poly_indices = model.sparse
        scval = model.encode_sum_constraint(self.levels)
        
        client = self.client
        lock_id, start_ts, end_ts = client.wait_for_lock()
        log.debug("Got device lock id %s. Wait time %f", lock_id, end_ts - start_ts)
        resp = None
        try:
            log.debug("Calling device with parameters relaxation_schedule %d sum_constraint %s lock_id %s solution_precision %f",
                      relaxation_schedule, scval, lock_id, precision)
            resp = client.process_job(poly_coefficients=poly_coefficients,
                                      poly_indices=poly_indices,
                                      relaxation_schedule=relaxation_schedule,
                                      sum_constraint = scval,
                                      lock_id = lock_id,
                                      solution_precision=precision)
            log.debug("Received response with status %s", resp["err_desc"])
            log.debug("Runtime %f resulting in energy %f", resp["runtime"], resp["energy"])
            log.debug("Distillation runtime %s resulting in energy %f", resp["distilled_runtime"], resp["distilled_energy"])
        finally:
            client.release_lock(lock_id=lock_id)
        if resp is not None:
            solution = resp["solution"]
            energy = resp["energy"]
            runtime = resp["runtime"]
            dirac3_sol = np.array(solution)
        else:
            raise RuntimeError("FAILED TO GET RESPONSE")
        return resp
