import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            summation = (left*left) + (right*right)
            if summation == c:
                return True
            elif summation < c:
                left+=1
            elif summation > c:
                right-=1
        return False
