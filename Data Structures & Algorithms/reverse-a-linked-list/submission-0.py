# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        vals = []
        curr = head
        while curr != None:
            vals.append(curr)
            curr = curr.next

        curr = vals.pop()
        new_head = curr
        while curr != head:
            prev = curr
            curr = vals.pop()
            prev.next = curr
            if curr == head:
                curr.next = None

        return new_head
     
