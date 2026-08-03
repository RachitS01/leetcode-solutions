class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []

        def dfs(current_node, current_path):
            if current_node == target:
                res.append(current_path[:])
                return 
            
            for neighbour in graph[current_node]:
                current_path.append(neighbour)
                dfs(neighbour,current_path)
                current_path.pop()

        dfs(0,[0])

        return res

            
