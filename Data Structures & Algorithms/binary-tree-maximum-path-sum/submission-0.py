# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(node):
            nonlocal max_sum
            if not node:
                return float("-inf")
            left_subtree_sum = dfs(node.left)
            right_subtree_sum = dfs(node.right)
             
            max_sum = max(max_sum,
                            node.val,
                            node.val+left_subtree_sum,
                            node.val+right_subtree_sum,
                            node.val+left_subtree_sum+right_subtree_sum)
            return max(node.val,node.val+left_subtree_sum,
                            node.val+right_subtree_sum)
        dfs(root)
        return max_sum