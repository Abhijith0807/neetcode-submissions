# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter,maxSubtree=self.treeDia(root)
        return(maxDiameter)

    def treeDia(self,root: Optional[TreeNode]):
        maxDia=0
        maxSubl=0
        if root:
            lDepth=0
            rDepth=0
            rlmaxDia=0
            rrmaxDia=0
            if root.left:
               rlmaxDia,rlmaxSub =self.treeDia(root.left)
               lDepth=lDepth+1+rlmaxSub
            if root.right:
                rrmaxDia,rrmaxSub=self.treeDia(root.right)
                rDepth=rDepth+1+rrmaxSub
            maxDia=max(maxDia,lDepth+rDepth,rlmaxDia,rrmaxDia)
            maxSubl=max(maxSubl,lDepth,rDepth)
            return(maxDia,maxSubl)
        else:
            return(maxDia,maxSub)

        