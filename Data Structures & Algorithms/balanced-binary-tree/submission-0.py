# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        BalanceCheck,maxHeight=self.checkBalanced(root)
        return(BalanceCheck)
    def checkBalanced(self, root: Optional[TreeNode]):
        maxHeight=0
        if root:
            lDepth=0
            rDepth=0
            lcond=True
            rcond=True
            if root.left:
                lcond,rlDepth=self.checkBalanced(root.left)
                lDepth=lDepth+1+rlDepth
            if root.right:
                rcond,rrDepth=self.checkBalanced(root.right)
                rDepth=rDepth+1+rrDepth
            if abs(lDepth-rDepth)<=1:
                return(True and lcond and rcond,max(lDepth,rDepth))
            else:
                return(False,max(lDepth,rDepth))
        else:
            return(True,maxHeight)