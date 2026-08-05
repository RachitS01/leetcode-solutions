import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        
        unique_edges = {}
        for u, v, w in edges:
            if (u, v) not in unique_edges or w < unique_edges[(u, v)]:
                unique_edges[(u, v)] = w
                
      
        u = np.array([edge[0] for edge in unique_edges.keys()])
        v = np.array([edge[1] for edge in unique_edges.keys()])
        w = np.array(list(unique_edges.values()))
        
        
        forward_graph = csr_matrix((w, (u, v)), shape=(n, n))
        reverse_graph = csr_matrix((w, (v, u)), shape=(n, n))
       
        dist1 = dijkstra(forward_graph, indices=src1)

        if dist1[dest] == np.inf:
            return -1
            
        dist2 = dijkstra(forward_graph, indices=src2)
        if dist2[dest] == np.inf:
            return -1
            
        dist_dest = dijkstra(reverse_graph, indices=dest)
 
        total_dist = dist1 + dist2 + dist_dest
        min_weight = np.min(total_dist)
        
        return int(min_weight) if min_weight != np.inf else -1
