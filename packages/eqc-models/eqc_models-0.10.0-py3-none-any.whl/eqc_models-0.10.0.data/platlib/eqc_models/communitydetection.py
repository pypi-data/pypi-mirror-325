# (C) Quantum Computing Inc., 2024.
import numpy as np
import networkx as nx
from .graphs import GraphModel

class CommunityDetectionModel(GraphModel):
    """ 
    This model is the generic n-community model, which requires enforcing 
    membership to a single community
    
    """

    def __init__(self, G : nx.Graph, num_communities : int):
        super(CommunityDetectionModel, self).__init__(G)
        self.cnum_communities = num_communities

    def build(self):
        # num_nodes = len(self.G.nodes)
        # num_variables = num_nodes * self.num_communities
        # lhs = np.zeros((num_nodes, num_variables), dtype=np.int32)
        # rhs = np.ones((num_nodes, 1), dtype=np.int32)
        # for i in range(num_nodes):
        #     lhs[i, 3*i:3*(i+1)] = 1
        # self.constraints = lhs, rhs
        raise NotImplementedError("Community Detection is not implemented yet")