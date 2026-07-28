class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z_arr = [0]*n
        left = 0
        right = 0

        for i in range(1,n):
            if i <= right:
                z_arr[i] = min(right - i + 1, z_arr[i -left])

            while i + z_arr[i] < n and s[z_arr[i]] == s[i+ z_arr[i]]:
                z_arr[i] +=1

            
            if i + z_arr[i] -1 > right:
                left = i
                right = i+ z_arr[i] -1

        return sum(z_arr) + n

