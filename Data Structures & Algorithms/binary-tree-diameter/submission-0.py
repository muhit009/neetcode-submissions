# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(current):
            if not current:
                return 0
            l = dfs(current.left)
            r = dfs(current.right)
            self.result = max(self.result, l+r)
            return 1+max(l,r)
        dfs(root)
        return self.result

        