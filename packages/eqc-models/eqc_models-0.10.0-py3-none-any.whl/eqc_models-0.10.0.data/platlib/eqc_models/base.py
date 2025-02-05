import os
import logging
from typing import (Dict, List, Tuple)
import numpy as np
from eqc_direct.client import EqcClient

log = logging.getLogger(name=__name__)

# base class 
class EqcModel:
    """ EqcModel subclasses must provide these properties/methods. 
    
    :decode: takes a raw solution and translates it into the original problem
      formulation 
    :H: property which returns a Hamiltonian operator 
    :levels: property to set the number of levels in each qudit
    :qudit_limits: maximjm value permitted for each qudit """

    _levels = 100
    _domains = None
    _H = None
    _machine_slacks = 0
    
    def decode(self, solution : np.ndarray) -> np.ndarray:
        """ Interpret the solution given the norm value and domains """
        
        # ignore any slacks that may have been added during encoding
        solution = solution[:self.n]
        if self._domains is not None:
            multipliers = self.domains / self.sum_constraint
        else:
            multipliers = self.sum_constraint / np.sum(solution)
        
        return multipliers * solution
    
    def encode(self, norm_value:float=1000) -> np.ndarray:
        """ Encode Hamiltonian into the domain of the device """

        raise NotImplementedError()

    def encode_sum_constraint(self, levels):
        new_sc = self.n * (levels-1) * self.sum_constraint / (np.sum(self.domains))
        return new_sc

    @property
    def domains(self) -> np.array:
        return self._domains

    @domains.setter
    def domains(self, value):
        self._domains = value

    @property
    def n(self) -> int:
        return int(max(self.domains.shape))
    
    def processH(self, H : np.ndarray) -> np.ndarray:
        """ By default, do nothing to H """

        return H

    @property
    def H(self) -> Dict[str, np.ndarray]:
        """ Matrix of a quadratic operator with the first column containing
        the linear terms and the remaining columns containing a symmetric
        quadratic matrix"""
        return self._H

    @H.setter
    def H(self, value : Dict[str, np.ndarray]):
        """ The H setter ensures that matrices order 2 and above are symmetric """

        H = self.processH(value)
        self._H = H

    @property
    def sparse(self) -> Tuple[np.ndarray, np.ndarray]:
        H = self.H
        coeff = []
        idx = []
        poly_orders = {"C": 1, "J": 2, "T": 3, "Q": 4, "P": 5}
        key_len = max([poly_orders[k] for k, v in H.items() if v is not None])
        
        
    @property
    def machine_slacks(self):
        """ Number of slack qudits to add to the model """
        return self._machine_slacks

    @machine_slacks.setter
    def machine_slacks(self, value:int):
        assert int(value) == value, "value not integer"
        self._machine_slacks = value

class ModelSolver:
    """ Provide a common interface for solver implementations. 
    Store a model, implement a solve method."""

    def __init__(self, model : EqcModel, levels : int = 200):
        self.model = model
        self._levels = levels

    def solve(self, *args, **kwargs) -> Dict:
        raise NotImplementedError()

    @property
    def levels(self) -> int:
        """ This integer value indicates the number of distinct 
        states each qudit can represent. These levels are separated
        by some constant value with the first level taking the value 0. """
        return self._levels

    @levels.setter
    def levels(self, value : int):
        self._levels = value
