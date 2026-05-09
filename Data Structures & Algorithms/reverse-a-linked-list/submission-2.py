# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_val = head
        prev_val = None

        while cur_val is not None:
            next_node = cur_val.next
            
            cur_val.next = prev_val

            prev_val = cur_val

            cur_val = next_node
        return prev_val


        




        