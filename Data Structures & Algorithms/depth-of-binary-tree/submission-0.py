# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        def length(node):
            if node != None:
                if length(node.left) > length(node.right):
                    return 1 + length(node.left)
                else:
                    return 1 + length(node.right)
        
            elif node == None:
                return 0 



        return length(node)