# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(root):
            if not root:
                return 0
            
            l = r = 0
            if root.left:
                l = balanced(root.left) + 1
            if root.right:
                r = balanced(root.right) + 1
            
            if  l > r+1 or r > l+1:
                self.is_balanced = False
            return max(l, r)

        balanced(root)
        return self.is_balanced