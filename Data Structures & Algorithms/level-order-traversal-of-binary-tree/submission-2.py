# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = root
        res = []

        queue = deque()
        queue.append(cur)

        if not root:
            return res
        while queue:
            res.append([])
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    res[-1].append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)


        return res
