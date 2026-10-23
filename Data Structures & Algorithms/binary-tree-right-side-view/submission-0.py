# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #do bfs, go level by level and add the right most to the queue

        #add nodes on curent floor to queue, left to right. add the last node to queue

        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            valid = None
            for i in range(len(q)):
                cur = q.popleft()
                
                if cur == None:
                    continue
                q.append(cur.left)
                q.append(cur.right)
                valid = cur
            if valid:
                res.append(valid.val)
            print(res)

        return res
