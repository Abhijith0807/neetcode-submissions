# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self,root):
        order=list()
        if root.left:
            leftsubtree=self.inorderTraversal(root.left)
            order.extend(leftsubtree)
        order.append(root.val)
        if root.right:
            rightsubtree=self.inorderTraversal(root.right)
            order.extend(rightsubtree)
        return(order)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder=self.inorderTraversal(root)
        return(inorder[k-1])
        