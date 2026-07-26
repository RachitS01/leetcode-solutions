class Solution:
    maxn = 100001
    ans = [0]*maxn

    arr = [1,2,2]
    curr_read = 2

    while len(arr) < maxn:
        nextnum = 3 - arr[-1]
        arr.extend([nextnum]*arr[curr_read])
        curr_read +=1

    ones_count = 0
    for i in range(1, maxn):
        if arr[i-1] == 1:
            ones_count += 1
        ans[i] = ones_count

    def magicalString(self, n: int) -> int:
        
        return self.ans[n]
