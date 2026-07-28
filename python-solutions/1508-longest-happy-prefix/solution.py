class Solution:
    def longestPrefix(self, s: str) -> str:
        base = 31
        mod = (10**9 + 7)
        back = 0
        prefix_hash = 0
        suffix_hash = 0
        n = len(s)
        power = 1
        best_len = -1
        for i in range(n-1):
            front = s[i]
            val_front = ord(front) - ord('a') + 1

            back = s[n-1-i]
            val_back = ord(back) - ord('a') + 1
            

            prefix_hash = (prefix_hash*base + val_front)%mod
            suffix_hash = (suffix_hash + val_back*power)%mod

            if suffix_hash == prefix_hash:
                best_len = i

            power = (power*base)%mod

            
        string = s[:best_len+1]
        print(string)

        return string
            


