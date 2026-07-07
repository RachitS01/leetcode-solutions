class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        heights.append(0)
        for i,current_h in enumerate(heights):
            while stack and current_h < heights[stack[-1]]:
                popped_index = stack.pop()
                height = heights[popped_index]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                maxarea = max(maxarea,width*height)
            stack.append(i)
        return maxarea
