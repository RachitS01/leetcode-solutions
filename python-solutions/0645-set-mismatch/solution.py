class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S_n = n * (n + 1) // 2
        S_n2 = n * (n + 1) * (2 * n + 1) // 6

        S_arr = sum(nums)
        S_arr2 = sum(x * x for x in nums)

        diff1 = S_n - S_arr
        diff2 = S_n2 - S_arr2

        sum_xy = diff2 // diff1

        missing = (diff1 + sum_xy) // 2
        duplicate = missing - diff1

        return [duplicate, missing]
