import numpy as np

class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
      
        _, counts = np.unique(nums, return_counts=True)
      
        return int(np.sum(counts * np.arange(len(counts))))
