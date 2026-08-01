class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tracker = [False]*n
        for _,to in edges:
            tracker[to] = True
        return [i for i in range(n) if not tracker[i]]
