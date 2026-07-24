class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]

        while len(ans) < n:
            odd = [2*x - 1 for x in ans]
            even = [2*x for x in ans]

            ans = odd + even

        return [x for x in ans if x <= n]
      
