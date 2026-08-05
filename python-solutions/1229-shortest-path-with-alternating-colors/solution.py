class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]
        answer = [-1]*n
        answer[0] = 0
        visited = set()

        queue = deque()
        queue.append((0,0,"red"))
        queue.append((0,0,"blue"))
        visited.add((0,"red"))
        visited.add((0,"blue"))
        print(queue)
        print(visited)
        
        for a,b in redEdges:
            red_graph[a].append(b)
        for u,v in blueEdges:
            blue_graph[u].append(v)


        while queue:
            node, distance, colour = queue.popleft()

            if colour == "red":
                for neighbour in blue_graph[node]:
                    if (neighbour,"blue") not in visited:
                        visited.add((neighbour,"blue"))

                        if answer[neighbour] == -1:
                            answer[neighbour] = distance + 1
                        queue.append((neighbour,distance+1,"blue"))
            else:
                for neighbour in red_graph[node]:
                    if (neighbour,"red") not in visited:
                        visited.add((neighbour,"red"))

                        if answer[neighbour] == -1:
                            answer[neighbour] = distance+ 1
                        queue.append((neighbour,distance+1,"red"))

        return answer



       
