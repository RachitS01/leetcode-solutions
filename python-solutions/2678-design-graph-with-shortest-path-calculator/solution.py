import heapq

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]) -> None:
        from_node, to_node, cost = edge
        self.adj[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        inf = 10**15
        dist = [inf] * self.n
        dist[node1] = 0

        queue = [(0, node1)]
        
        
        adj = self.adj 
        heappop = heapq.heappop
        heappush = heapq.heappush

        while queue:
            current_cost, current_node = heappop(queue)

            if current_node == node2:
                return current_cost

            if current_cost > dist[current_node]:
                continue

          
            for neighbour, cost in adj[current_node]:
                new_cost = current_cost + cost

                if new_cost < dist[neighbour]:
                    dist[neighbour] = new_cost
                    heappush(queue, (new_cost, neighbour))

        return -1
