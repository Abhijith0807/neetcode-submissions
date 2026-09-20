# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempptr=head
        llen=0
        while tempptr:
            tempptr=tempptr.next
            llen+=1
        front=llen-n+1
        cnt=1
        curr=head
        prev=None
        while cnt!=front:
            prev=curr
            curr=curr.next
            cnt+=1
        if cnt!=1:
            prev.next=curr.next
            return(head)
        else:
            return(head.next)        