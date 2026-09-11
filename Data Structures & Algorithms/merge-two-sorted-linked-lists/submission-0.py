# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        #make a new list, dummy is the new start
        dummy = ListNode()
        head = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head = head.next
                head1 = head1.next
            else:
                head.next = head2
                head = head.next
                head2 = head2.next
        head.next = head1 or head2
        return dummy.next
                