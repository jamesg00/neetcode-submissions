# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            #saving the pointer
            next_node = curr.next
            #reverse our list
            curr.next = prev
            #move prev forward
            prev = curr
            #mov current forward
            curr = next_node
    
        #return previous
        return prev 












        