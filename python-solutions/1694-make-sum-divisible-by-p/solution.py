class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p


        if target_rem == 0:
            return 0
        
        hash_map = {0:-1}

        current_sum = 0
        min_length = len(nums)

        for index,num in enumerate(nums):
            current_sum += num
            current_rem = current_sum % p

            needed_rem = (current_rem - target_rem)%p

            if needed_rem in hash_map:
                distance = index  - hash_map[needed_rem]
                min_length = min(min_length, distance)

            hash_map[current_rem] = index

        if min_length == len(nums):
            return -1
        else:
            return min_length
