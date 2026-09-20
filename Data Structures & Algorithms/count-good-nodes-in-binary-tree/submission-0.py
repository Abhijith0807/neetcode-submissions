# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getgoodNodes(self,root: TreeNode, maxval: int) -> int:
        while root:
            if root.val>=maxval:
                return(1+self.getgoodNodes(root.left,root.val)+self.getgoodNodes(root.right,root.val))
            else:
                return(0+self.getgoodNodes(root.left,maxval)+self.getgoodNodes(root.right,maxval))
        return(0)
    def goodNodes(self, root: TreeNode) -> int:
        count=1
        maxval=root.val
        if root.left:
            count=count+self.getgoodNodes(root.left,maxval)
        if root.right:
            count=count+self.getgoodNodes(root.right,maxval)
        return(count)
        