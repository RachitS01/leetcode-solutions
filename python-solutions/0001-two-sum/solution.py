class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            current_num = nums[i]
            difference = target - current_num

            if difference in hash_map:
                return [hash_map[difference],i]
            else:
                hash_map[current_num] = i 
