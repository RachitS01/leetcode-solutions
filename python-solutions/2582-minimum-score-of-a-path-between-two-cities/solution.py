class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))

        self.min_score = [float('inf')] * (size + 1) 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, distance):
        root_x = self.find(x)
        root_y = self.find(y)

        smallest_road = min(self.min_score[root_x], self.min_score[root_y], distance)

        if root_x != root_y:
            self.parent[root_y] = root_x
            

        self.min_score[root_x] = smallest_road


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        uf = UnionFind(n)
        
        for u, v, distance in roads:
            uf.union(u, v, distance)

        return uf.min_score[uf.find(1)]
