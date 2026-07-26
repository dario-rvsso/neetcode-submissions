# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        if h1 == None:
            return h2
        if h2 == None:
            return h1
        if h1.val < h2.val:
            h1.next = self.mergeTwoLists(h1.next, h2)
            return h1
        else:
            h2.next = self.mergeTwoLists(h1, h2.next)
            return h2
    

             