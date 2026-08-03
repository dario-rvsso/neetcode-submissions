# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.values = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.values.append(root.val)
            inorder(root.right)
            return
        
        inorder(root)
        return self.values[k-1]

        