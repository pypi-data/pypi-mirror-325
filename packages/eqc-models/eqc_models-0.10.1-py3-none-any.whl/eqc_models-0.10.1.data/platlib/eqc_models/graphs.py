from typing import List
import networkx as nx
from .quadraticmodel import QuadraticModel

class GraphModel(QuadraticModel):

    def __init__(self, G : nx.Graph):
        self.G = G

class TwoPartitionModel(GraphModel):
    """ Create a model where the variables are node-based """

    @property
    def variables(self) -> List[str]:
        """ Provide a variable name to index lookup, order enforced by sorting the list before returning """
        names = [node.name for node in self.G.nodes]
        names.sort()
        return names
    
class EdgeModel(GraphModel):
    """ Create a model where the variables are edge-based """

    @property
    def variables(self) -> List[str]:
        """ Provide a variable name to index lookup, order enforced by sorting the list before returning """
        names = [f"({u},{v})" for u, v in self.G.edges]
        names.sort()
        return names
