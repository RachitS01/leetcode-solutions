class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        store = 0
        for element in nums:
            if element == 1:
                count = count + 1
            else:
                if store <= count:
                    store = count
                count = 0
        if count < store:
            return store
        elif count >= store:
            return count
