# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        
        def diameter(node):
            if not node:
                return -1
            left, right = diameter(node.left), diameter(node.right)
            self.ans = max(self.ans, 2 + left + right)
            return 1 + max(left, right)
        
        diameter(root)
        return self.ans