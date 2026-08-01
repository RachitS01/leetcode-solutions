class UnionFind:
    def __init__(self, n, restrictions):
        self.parent = list(range(n))
        
        self.members = [{i} for i in range(n)]
        

        self.enemies = [set() for _ in range(n)]
        
   
        for u, v in restrictions:
            self.enemies[u].add(v)
            self.enemies[v].add(u)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return True 
        
       
        if not self.members[root_v].isdisjoint(self.enemies[root_u]):
            return False
            
        
        self.parent[root_v] = root_u
        
       
        self.members[root_u] |= self.members[root_v]
        self.enemies[root_u] |= self.enemies[root_v]
        
        return True

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        uf = UnionFind(n, restrictions)
        
       
        return [uf.union(u, v) for u, v in requests]
