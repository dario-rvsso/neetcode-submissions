# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rc = []
        fifo = deque()

        if root:
            fifo.append(root)

        while len(fifo) > 0:
            size = len(fifo)
            for i in range(size):
                node = fifo.popleft()
                if i == size - 1:
                    rc.append(node.val)
                if node.left:
                    fifo.append(node.left)
                if node.right:
                    fifo.append(node.right)
        return rc


