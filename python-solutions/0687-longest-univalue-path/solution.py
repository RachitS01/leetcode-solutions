# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solve(current,parent):
            nonlocal ans
            if current == None:
                return 0
            
            left = solve(current.left,current.val)
            right = solve(current.right,current.val)

            ans = max(ans,left+right)

            return max(left,right)+1 if current.val == parent else 0


        solve(root,-1)

        return ans

