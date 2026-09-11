# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        def invert(node):
            if node != None:
                node.left, node.right = node.right, node.left
                node.left = invert(node.left)
                node.right = invert(node.right)
                return node
            
            else:
                return None
        node = invert(node)
        return node