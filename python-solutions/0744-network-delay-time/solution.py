import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
            
 
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        pq = [(0, k)]
        
    
        while pq:
            time, node = heapq.heappop(pq)
            
      
            if time > dist[node]:
                continue
                
            for neighbor, weight in adj[node]:
                new_time = time + weight
             
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
                    
      
        max_time = max(dist[1:])
        
        return max_time if max_time < float('inf') else -1
