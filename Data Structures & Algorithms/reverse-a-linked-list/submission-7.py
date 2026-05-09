# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_val = head
        prev_val = None

        while cur_val:
            #save next node
            next_node = cur_val.next
            #flips the arrow
            cur_val.next = prev_val
            #move prev val up to cur_val
            prev_val = cur_val

            #move cur_val to the next node
            cur_val = next_node
        #keeps iterating until we flip every node
        #in reverse 
        return prev_val





        