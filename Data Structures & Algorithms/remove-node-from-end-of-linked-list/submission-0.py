# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #dump into array, remove nth item from the end

        #linked list appraoch:

        cur = head
        counter = 0

        while cur:
            counter +=1;
            cur = cur.next
        
        print(counter)
        
        #Counter holds number of nodes in the list, n is the node from the end of the list that we need to detach from the list

        count = counter-n

        if count ==0:
            return head.next
        prev = head
        cur = head
        for i in range(count):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next


        return head
            
