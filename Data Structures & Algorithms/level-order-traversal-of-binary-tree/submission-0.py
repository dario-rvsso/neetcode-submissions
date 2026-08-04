# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rc = []
        tmp = []
        level = 0
        fifo = deque()

        if root:
            fifo.append(root)

        while len(fifo) > 0:
            size = len(fifo)
            tmp = []
            for _ in range(size):
                node = fifo.popleft()
                if node.left:
                    fifo.append(node.left)
                if node.right:
                    fifo.append(node.right)
                tmp.append(node.val)
            rc.append(tmp)

        return rc
