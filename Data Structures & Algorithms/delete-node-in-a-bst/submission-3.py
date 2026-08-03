# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            if root.left != None and root.right == None:
                return root.left
            elif root.left == None and root.right != None:
                return root.right
            elif root.left == None and root.right == None:
                return None
            else:
                tmp = root.right
                while tmp.left != None:
                    tmp = tmp.left
                root.right = self.deleteNode(root.right, tmp.val)
                root.val = tmp.val
                return root
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
        