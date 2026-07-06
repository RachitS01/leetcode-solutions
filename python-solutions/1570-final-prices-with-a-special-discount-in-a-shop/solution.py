class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                popped_index = stack.pop()
                answer[popped_index] -= prices[i]
            stack.append(i)
        return answer
