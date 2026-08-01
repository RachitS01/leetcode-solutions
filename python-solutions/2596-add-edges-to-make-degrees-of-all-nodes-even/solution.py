class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        odd_nodes = []
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u) 
            
        for i in range(len(graph)):
            if len(graph[i]) %2 != 0:
                odd_nodes.append(i)

        if len(odd_nodes) == 0: return True

        elif (len(odd_nodes) == 1 or len(odd_nodes) == 3 or len(odd_nodes) > 4) : return False

        elif len(odd_nodes) == 2:
            A = odd_nodes[0]
            B = odd_nodes[1]
            if A not in graph[B]:
                return True
            else:
                for i in range(1,n+1):
                    if i != A and i != B:
                        if A not in graph[i] and B not in graph[i]:
                            return True
                return False

        elif len(odd_nodes) == 4:
            A, B, C, D = odd_nodes
            if (A not in graph[B]) and (C not in graph[D]): return True
            elif (A not in graph[C]) and (B not in graph[D]): return True
            elif(A not in graph[D]) and (B not in graph[C]):return True
            else: return False
        
        return False
