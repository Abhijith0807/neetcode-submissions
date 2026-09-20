# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        while p and q:
            if p.val!=q.val:
                return(False)
            else:
                lbool=self.isSameTree(p.left,q.left)
                rbool=self.isSameTree(p.right,q.right)
                return(lbool and rbool)
        if p or q:
            return(False)
        else:
            return(True)