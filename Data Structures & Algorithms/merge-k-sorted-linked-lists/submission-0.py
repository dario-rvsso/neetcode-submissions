# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [[]]:
            return None
 
        e = [float("inf")] * len(lists)
        p = [None] * len(lists)
        start = ListNode(None)

        for i in range(len(lists)):
            if lists[i] != None:
                p[i] = lists[i]
                e[i] = p[i].val

        curr = start
        while True:
            c = min(e)
            if c != float("inf"):
                idx = e.index(c)
                tmp = ListNode(c)
                curr.next = tmp
                curr = curr.next

            if p[idx].next != None:
                p[idx] = p[idx].next
                e[idx] = p[idx].val
            else:
                p[idx] = None
                e[idx] = float("inf")
            
            if e.count(float("inf")) >= len(e):
                break

        return start.next
