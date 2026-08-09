class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        
        nodes = [None] * 100001 
        
        has_parent = bytearray(100001) 
        
        for p, c, is_left in descriptions:
            
            if nodes[p] is None:
                nodes[p] = TreeNode(p)
            if nodes[c] is None:
                nodes[c] = TreeNode(c)
                
            if is_left == 1:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            
            has_parent[c] = 1

        for p, c, is_left in descriptions:
            if has_parent[p] == 0:
                return nodes[p]
