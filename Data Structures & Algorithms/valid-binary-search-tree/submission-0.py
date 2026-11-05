# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left, right):
            if not node:
                return True
            val =node.val
            if val<=left or val>= right:
                return False
            
            if not helper(node.left, left, val):
                return False
            
            if not helper(node.right, val, right):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))
        