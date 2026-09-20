"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashNode=dict()
        if not head:
            return(head)
        def deepcopy(head):
            currNode=Node(head.val,None,None)
            hashNode[head]=currNode
            if head.next==None:
                currNode.next=None
            else:
                currNode.next=deepcopy(head.next)
            if head.random==None:
                currNode.random=None
            else:
                currNode.random=hashNode[head.random]
            return(currNode)

        return(deepcopy(head))