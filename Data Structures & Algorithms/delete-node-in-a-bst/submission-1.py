# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = None
        curr = root

        if curr == None:
            return None

        if curr.val == key:
            if curr.left != None and curr.right == None:
                return curr.left
            elif curr.left == None and curr.right != None:
                return curr.right
            elif curr.left == None and curr.right == None:

                return None
            else:
                b = curr.right
                while b.left != None:
                    b = b.left
                curr.right = self.deleteNode(curr.right, b.val)
                curr.val = b.val
                return curr
        else:
            prev = curr
            if key < curr.val:
                curr = self.deleteNode(curr.left, key)
                prev.left = curr  
            else: 
                curr = self.deleteNode(curr.right, key)
                prev.right = curr
            return root



        