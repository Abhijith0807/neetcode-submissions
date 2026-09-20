# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,preorder,left,right):
        if left > right or self.preindex>=len(preorder):
            return None
        inorderpos = self.Map[preorder[self.preindex]]
        node  = TreeNode(preorder[self.preindex])
        self.preindex+=1
        node.left = self.dfs(preorder,left,inorderpos-1)
        if not node.left:
            self.preindex-=1
        self.preindex+=1
        node.right = self.dfs(preorder,inorderpos+1,right)
        if not node.right:
            self.preindex-=1
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.Map = {j:i for i,j in enumerate(inorder)}
        self.preindex = 0
        root = self.dfs(preorder,0,len(preorder)-1)
        return root