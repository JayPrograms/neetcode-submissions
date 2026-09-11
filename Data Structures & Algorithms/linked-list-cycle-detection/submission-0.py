# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        i = 0
        while current:
            if current.val >= i:
                current.val = i
                i = i +1
                current = current.next
            else:
                return True
        return False

