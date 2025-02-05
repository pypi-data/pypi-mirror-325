from typing import Tuple
import numpy as np
from .base import EqcModel

class QuadraticMixIn:
    C = None
    J = None

    def encode(self, levels:int=200, norm_value:float=None, dtype=np.float32) -> np.ndarray:
        """ 
        Encode Hamiltonian into the domain of the device 

        The encoding method can be tuned using levels or norm_value. The parameter 
        levels and the member self.domains are used to generate a vector t such that
        $$
        x = ts
        $$
        thus,
        $$
        h^Tx + x^TJx = h^T(ts) + (ts)^TJ(ts) = (th)^Ts + s^T(t\\cross tJ)s
        $$
        
        """

        n = max(self.domains.shape)
        J = self.J
        C = self.C
        if norm_value is None:
            max_level = levels - 1
            multipliers = (self.domains) / max_level
            J = np.array(np.outer(multipliers, multipliers) * J)
            # h = np.multiply(h[:,0], multipliers)
            C *= multipliers
            C = C.reshape((n, 1))
        else:
            # normalize the operator
            max_val_J = np.max(np.abs(J))
            max_val_C = np.max(np.abs(C))
            if max_val_J > max_val_C:
                max_val = max_val_J
            else:
                max_val = max_val_C
            C /= max_val
            C *= norm_value
            J /= max_val
            J *= norm_value
        # make J symmetric
        J += J.T
        J /= 2
        # return operator in hJ format
        H = np.hstack([C, J]).astype(dtype)

        if self.machine_slacks > 0:
            machine_slacks = self.machine_slacks
            n = H.shape[0]
            Hslack = np.zeros((n+machine_slacks, n+machine_slacks+1), dtype=dtype)
            Hslack[:n, :n+1] = H
            H = Hslack
    
        return np.array(H)
        
    @property
    def sparse(self) -> Tuple[np.ndarray, np.ndarray]:
        """ Put the linear and quadratic terms in a sparse format 
        
        :returns: coefficients : List, indices : List
        """
        C, J = self.H
        n = self.n
        indices = []
        coefficients = []
        # build a key (ordered tuple of indices) of length 2 for each element
        for i in range(n):
            if C[i,0] != 0:
                key = (0, i+1)
                indices.append(key)
                coefficients.append(C[i,0])
        # make J upper triangular
        J = np.triu(J) + np.tril(J, -1).T
        for i in range(n):
            for j in range(i, n):
                val = J[i, j]
                if val != 0:
                    key = (i+1, j+1)
                    indices.append(key)
                    coefficients.append(val)
        return np.array(coefficients, dtype=np.float32), np.array(indices, dtype=np.int32)
    
    def evaluate(self, solution: np.ndarray, decode:bool=False, levels:int=200) -> float:
        """ 
        Evaluate the solution using the original operator. The decode
        and levels parameters control the decoding of the solution. Without
        specifying decode, the evaluation of the operator is done with the
        solution provided.
         
        """
        H = self.H
        h, J = H[:, 0], H[:, 1:]
        if decode:
            sol = self.decode(solution)
        else:
            sol = solution
        return np.squeeze(sol.T@J@sol + h.T@sol)

class QuadraticModel(QuadraticMixIn, EqcModel):
    """ Provides a quadratic operator and device sum constraint support """

    def __init__(self, C : np.ndarray, J : np.ndarray, sum_constraint : float):
        self._C = C
        self._J = J
        self._sum_constraint = sum_constraint
    
    @property
    def H(self):
        return self._C, self._J
    
    def check_constraint(self, solution: np.array) -> bool:
        """ Evaluate the solution against the original sum constraint """
        return np.sum(solution) == self.sum_constraint
    
    @property
    def sum_constraint(self) -> int:
        """ Integer value which all qudits must sum to.
        The value must be less than or equal to  n * base for
        the model to make sense. """

        return self._sum_constraint

    @sum_constraint.setter
    def sum_constraint(self, value : int):
        self._sum_constraint = value
