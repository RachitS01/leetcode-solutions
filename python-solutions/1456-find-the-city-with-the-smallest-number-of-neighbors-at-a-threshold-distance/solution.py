class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        inf = 10**16
        dist = [inf]*n
        dist[0] = 0

        for from_i, to_i, weight in edges:
            adj[from_i].append((to_i,weight))
            adj[to_i].append((from_i,weight))

        queue = [(0,0)]
        cities_reachable = inf
        count = 0
        inf = 10**15

        heappop = heapq.heappop
        heappush = heapq.heappush


        def dijkstra(source):
            
            dist = [inf] * n
            dist[source] = 0
            reachable_count = -1

            queue = [(0, source)]
        

            while queue:
                current_cost, current_node = heappop(queue)

                if current_cost > dist[current_node]:
                    continue

            
                for neighbour, cost in adj[current_node]:
                    new_cost = current_cost + cost

                    if new_cost < dist[neighbour] and new_cost <= distanceThreshold:
                        dist[neighbour] = new_cost
                        heappush(queue, (new_cost, neighbour))

            
            for i in dist:
                if i <= distanceThreshold:
                    reachable_count += 1

            return reachable_count


        min_reachable = inf
        best_city = -1

        for i in range(n):
            reachable_count = dijkstra(i)
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                best_city = i

        return best_city
                

        
            


                
            
