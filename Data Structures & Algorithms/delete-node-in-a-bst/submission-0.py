class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        lr = True
        prev = None
        curr = root

        while curr != None:
            if curr.val == key:
                if curr.left == None and curr.right != None:
                    if prev == None: return curr.right
                    if lr == True:
                        prev.left = curr.right
                    else:
                        prev.right = curr.right
                    break
                elif curr.right == None and curr.left != None:
                    if prev == None: return curr.left
                    if lr == True:
                        prev.left = curr.left
                    else:
                        prev.right = curr.left
                    break
                elif curr.left == None and curr.right == None:
                    if prev == None:
                        return None
                    if lr == True:
                        prev.left = None
                    else:
                        prev.right = None
                    break
                else:
                    sprv = curr
                    swap = curr.left
                    while swap.right != None:
                        sprv = swap
                        swap = swap.right
                    curr.val = swap.val
                    if sprv == curr:
                        sprv.left = swap.left
                    else:
                        sprv.right = swap.left
                    break
            else:
                if key < curr.val:
                    lr = True
                    prev = curr
                    curr = curr.left
                else:
                    lr = False
                    prev = curr
                    curr = curr.right
        return root