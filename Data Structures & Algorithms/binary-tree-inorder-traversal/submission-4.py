# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, root, traversal):
        if not root:
            return traversal

        self.inorder(root.left, traversal)
        traversal.append(root.val)
        self.inorder(root.right, traversal)
        return traversal

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        traversal = self.inorder(root, traversal)
        return traversal
