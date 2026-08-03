# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0:
            return None
        
        root = preorder[0]
        pivot = inorder.index(root)
        
        nodel = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        noder = self.buildTree(preorder[pivot+1:], inorder[pivot+1:]) 

        node = TreeNode(root, nodel, noder)
        return node



