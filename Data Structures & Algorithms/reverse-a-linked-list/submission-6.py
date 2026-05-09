# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev_val = None

        while curr:
            nextVal = curr.next

            curr.next = prev_val

            prev_val = curr

            curr = nextVal
        return prev_val 

    




        