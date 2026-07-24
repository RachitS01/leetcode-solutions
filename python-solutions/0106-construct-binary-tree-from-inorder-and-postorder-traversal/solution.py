# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        #mapping
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        
        def helper_fences(left,right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            mid = inorder_map[root_val]

            root.right = helper_fences(mid+1,right)
            root.left = helper_fences(left,mid-1)

            return root

        return helper_fences(0,len(inorder)-1)
