class unionFind:
    def __init__(self,size):
        self.parent  = [i for i in range(size)]

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = unionFind(n)
        for u,v in edges:
            uf.union(u,v)


        if uf.find(source) == uf.find(destination):
            return True
        else:
            return False

                    
                



