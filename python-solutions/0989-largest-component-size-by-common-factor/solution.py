import math
import collections

class UnionFind:
        def __init__(self,size):
            self.parent = [i for i in range(size)]

        def find(self,x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x != root_y:
                self.parent[root_y] = root_x
                return True
            return False


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_val = max(nums)

        spf = list(range(max_val + 1))
        p = 2
        while p * p <= max_val:
            if spf[p] == p: # If p is prime
                # Mark all multiples of p with p as their smallest prime factor
                for i in range(p * p, max_val + 1, p):
                    if spf[i] == i:
                        spf[i] = p
            p += 1

        uf = UnionFind(max_val+1)

        for num in nums:
            temp = num
            while temp > 1:
                prime_factor = spf[temp]
                uf.union(num, prime_factor)
                
                # Divide out all instances of this prime factor
                while temp % prime_factor == 0:
                    temp //= prime_factor

        group_count = collections.defaultdict(int)

        for num in nums:
            root = uf.find(num)
            group_count[root] += 1

        return max(group_count.values())
