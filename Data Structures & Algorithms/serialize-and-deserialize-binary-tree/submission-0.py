# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#question : when the left subtree stops and the right subtree stops?
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('#')
                return
            #preorder traversel (root - left -right)
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.idx = 0 
        def dfs():
            if values[self.idx] == "#":
                self.idx += 1
                return None
            node = TreeNode(int(values[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            


