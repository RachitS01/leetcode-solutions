import numpy as np
from scipy.ndimage import distance_transform_cdt

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        
        grid = 1 - np.array(isWater)
        
        
        result = distance_transform_cdt(grid, metric='taxicab')
        
     
        return result.tolist()
