class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack_op = []
        target_idx = 0
        for i in range(1,n+1):
            stack_op.append("Push")
            if i == target[target_idx]:
                target_idx += 1
            else:
                stack_op.append("Pop")
            if target_idx == len(target):
                break
        return stack_op
