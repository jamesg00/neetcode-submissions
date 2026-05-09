# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        #whle l1 and l2 exist
        while list1 and list2:
            #start appending l1 if smaller
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            #append l2 if smaller
            else:
                tail.next = list2
                list2 = list2.next
            #update tail 
            tail = tail.next
        #handles if there are no more vals in one list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        #dummy.next returns merged list 
        return dummy.next

        

