# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            
            if not node:
                return 0
            
            hleft = height(node.left)
            if hleft == -1:
                return -1
            
            hright = height(node.right)
            if hright == -1:
                return -1
            
            if abs(hleft - hright) > 1:
                return -1
            
            return max(hleft, hright) + 1    

        return height(root) != -1 