# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            node = TreeNode(val)
            return node

        lr = True
        prev = None
        curr = root
        while curr != None:
            if val < curr.val:
                lr = True
                prev = curr
                curr = curr.left
            elif val > curr.val:
                lr = False
                prev = curr
                curr = curr.right
        
        node = TreeNode(val)
        if lr == True:
            prev.left = node
        else:
            prev.right = node
        
        return root


        
        