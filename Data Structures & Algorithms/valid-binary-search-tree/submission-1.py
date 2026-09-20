# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validTree(self,node,maxVal,minVal):
        if node.val<=minVal or node.val>=maxVal:
            return False
        if node.left and node.right:
            return(self.validTree(node.left,node.val,minVal) and 
                    self.validTree(node.right,maxVal,node.val))
        elif node.left:
            return(self.validTree(node.left,node.val,minVal))
        elif node.right:
            return(self.validTree(node.right,maxVal,node.val))
        return True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validTree(root,float("infinity"),float("-infinity"))