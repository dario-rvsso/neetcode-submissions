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
        
        inl = inorder[:pivot]
        inr = inorder[pivot+1:]
        prex = preorder[1:]
        prel = prex[:len(inl)]
        prer = prex[len(inl):]

        nodel = self.buildTree(prel, inl)
        noder = self.buildTree(prer, inr) 

        node = TreeNode(root, nodel, noder)
        return node



