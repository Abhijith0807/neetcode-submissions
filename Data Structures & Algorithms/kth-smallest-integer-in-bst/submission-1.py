# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node,k):
        if not node:
            return
        self.dfs(node.left,k)
        if self.reached:
            return
        self.cnt+=1
        if self.cnt == k:
            self.res_val = node.val
            self.reached = True
            return
        self.dfs(node.right,k)
        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.reached = False
        self.res_val = -1
        self.dfs(root,k)
        return self.res_val