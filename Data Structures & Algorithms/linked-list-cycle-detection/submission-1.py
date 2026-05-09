# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #fast and slow pointers technique 
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy


        #if fasts exists, use fast.next.next to move fast
        #twice
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            #algorithm detects if slow and fast equal
            #if so ret true 
            if slow is fast:
                return True
        
        return False 




        
        