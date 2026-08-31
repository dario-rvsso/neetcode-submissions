# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twins = {}
        fast = head
        slow = head
        maxi = 0
        i = 0

        while fast and fast.next:
            fast = fast.next.next
            twins[i] = slow.val
            slow = slow.next
            i += 1
        while slow:
            i -= 1 
            twins[i] += slow.val
            slow = slow.next
        maxi = max(twins.values())

        return maxi
        