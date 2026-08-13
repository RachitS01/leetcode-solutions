class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        
        ans = [-1] * len(queries)
        
        
        waiting_list = [[] for _ in range(n)]
        
    
        for q_idx, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
                
         
            if a == b:
                ans[q_idx] = a
          
            elif heights[a] < heights[b]:
                ans[q_idx] = b
        
            else:
              
                waiting_list[b].append((heights[a], q_idx))
       
        min_heap = []
   
        for i, h in enumerate(heights):
            
           
            while min_heap and min_heap[0][0] < h:
                req_h, q_idx = heapq.heappop(min_heap)
                ans[q_idx] = i
                
          
            for query in waiting_list[i]:
                heapq.heappush(min_heap, query)
                
        return ans
