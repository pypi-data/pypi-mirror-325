import networkx as nx
import numpy as np
from .graphs import TwoPartitionModel

class MaxCutModel(TwoPartitionModel):

    def build(self):
        variables = self.variables
        n = len(variables)
        self.domains = np.ones((n,))
        
        J = np.zeros((n+1, n+1), dtype=np.float32)
        h = np.zeros((n+1,1), dtype=np.float32)
        for u, v in G.edges:
            J[u, v] += 1
            J[v, u] += 1
            J[u, u] = 1
            J[v, v] = 1
            h[u] -= 1
            h[v] -= 1
        J *= 1/t**2
        h *= 1/t
        H = np.hstack([h, J])
        return H

    @property
    def J(self) -> np.ndarray:
        if getattr(self, "_J", None) is None:
            self.build()
        return self._J

    @property
    def C(self) -> np.ndarray:
        if getattr(self, "C", None) is None:
            self.build()
        return self._C
    
def get_graph(n, d):
    """ Produce a repeatable graph with parameters n and d """

    seed = n * d
    return nx.random_graphs.random_regular_graph(d, n, seed)

def get_partition_graph(G, solution):
    """
    Build the partitioned graph, counting cut size 

    :parameters: G : nx.DiGraph, solution : np.ndarray
    :returns: nx.DiGraph, int
    
    """

    cut_size = 0
    Gprime = nx.DiGraph()
    Gprime.add_nodes_from(G.nodes)
    for i, j in G.edges:
        if solution[i] != solution[j]:
            cut_size+=1
        else:
            Gprime.add_edge(i, j)
    return Gprime, cut_size

def determine_solution(G, solution):
    """
    Use a simple bisection method to determine the binary solution. Uses
    the cut size as the metric.

    Returns the partitioned graph and solution.

    :parameters: G : nx.DiGraph, solution : np.ndarray
    :returns: nx.DiGraph, np.ndarray

    """

    solution = np.array(solution)
    lower = np.min(solution)
    upper = np.max(solution)
    best_cut_size = 0
    best_graph = G
    best_solution = None
    while upper > lower + 0.0001:
        middle = (lower + upper) / 2
        test_solution = (solution>=middle).astype(np.int32)
        Gprime, cut_size = get_partition_graph(G, test_solution)
        if cut_size > best_cut_size:
            best_cut_size = cut_size
            lower = middle
            best_solution = test_solution
            best_graph = Gprime
        else:
            upper = middle
    return best_graph, best_solution

def get_maxcut_H(G, t):
    """ 
    Return a Hamiltonian representing the Maximum Cut Problem. Scale the problem using `t`.
    Automatically adds a slack qudit.
    
    """
    n = len(G.nodes)
    J = np.zeros((n+1, n+1), dtype=np.float32)
    h = np.zeros((n+1,1), dtype=np.float32)
    for u, v in G.edges:
        J[u, v] += 1
        J[v, u] += 1
        J[u, u] = 1
        J[v, v] = 1
        h[u] -= 1
        h[v] -= 1
    J *= 1/t**2
    h *= 1/t
    H = np.hstack([h, J])
    return H