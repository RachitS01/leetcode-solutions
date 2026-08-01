from collections import defaultdict, deque

class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:    
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
               
        queue = deque([(0, 0, values[0], {0})])   
        best_state = {}    
        max_quality = 0
        
        while queue:
            node, time_spent, current_score, visited_nodes = queue.popleft()
              
            if node in best_state:
                prev_time, prev_score = best_state[node]
                if prev_time <= time_spent and prev_score > current_score:
                    continue       
        
            best_state[node] = (time_spent, current_score)
            
            if time_spent > maxTime:
                continue
                
            if node == 0:
                max_quality = max(max_quality, current_score)
        
            for neighbor, travel_time in graph[node]:                 
                new_visited = visited_nodes.copy()
                
                if neighbor not in visited_nodes:
                    new_visited.add(neighbor)
                    new_score = current_score + values[neighbor]
                else:
                    new_score = current_score
                queue.append((
                    neighbor, 
                    time_spent + travel_time, 
                    new_score, 
                    new_visited
                ))
                
        return max_quality
