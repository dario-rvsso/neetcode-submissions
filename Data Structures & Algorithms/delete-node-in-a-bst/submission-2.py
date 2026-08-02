# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
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
                tmp = curr.right
                while tmp.left != None:
                    tmp = tmp.left
                curr.right = self.deleteNode(curr.right, tmp.val)
                curr.val = tmp.val
                return curr
        else:
            if key < curr.val:
                curr.left = self.deleteNode(curr.left, key)
            else: 
                curr.right = self.deleteNode(curr.right, key)
            return curr



        