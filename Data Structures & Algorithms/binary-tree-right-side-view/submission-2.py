# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        res=list()
        q.append(root)
        if not root:
            return([])
        while q:
            temp=q[-1]
            res.append(temp.val)
            qlen=len(q)
            for i in range(qlen):
                tempr=q.popleft()
                if tempr.left:
                    q.append(tempr.left)
                if tempr.right:
                    q.append(tempr.right)
        return(res)
                
