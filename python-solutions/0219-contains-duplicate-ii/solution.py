class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == len(set(nums)):
            return False

        window = {}
        for index,value in enumerate(nums):
            if value in window and index- window[value] <= k:
                return True
            window[value] = index

        return False
