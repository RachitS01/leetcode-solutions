
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if not s:
            return s

        base = 26
        mod = (10**9+7)
        forward_hash = 0
        backward_hash = 0
        power = 1

        best_prefix_index = -1
        for i,char in enumerate(s):

            val = ord(char) - ord('a') + 1

            forward_hash = (forward_hash*base + val)%mod
            backward_hash = (backward_hash + val*power)%mod

            if forward_hash == backward_hash:
                best_prefix_index = i

            power = (power*base)%mod

        leftover = s[best_prefix_index+1:]

        return leftover[::-1] + s

        
