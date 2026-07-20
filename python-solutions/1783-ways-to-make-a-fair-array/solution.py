class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        count = 0
        total_even = sum(nums[0::2])
        total_odd = sum(nums[1::2])
        
        prefix_even = 0
        prefix_odd = 0

        for i in range(len(nums)):
            

            if i % 2 == 0:
                suffix_even = total_even - prefix_even - nums[i]
                suffix_odd  = total_odd - prefix_odd
            else:
                suffix_even = total_even - prefix_even
                suffix_odd  = total_odd - prefix_odd - nums[i]


            new_even_sum = prefix_even + suffix_odd
            new_odd_sum  = prefix_odd + suffix_even


            if new_even_sum == new_odd_sum:
                count += 1
                

            if i % 2 == 0:
                prefix_even += nums[i]
            else:
                prefix_odd += nums[i]
        
        return count
