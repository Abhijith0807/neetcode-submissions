# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondptr=slow.next
        slow.next=None
        prev=None
        while secondptr:
            temp=secondptr.next
            secondptr.next=prev
            prev=secondptr
            secondptr=temp
        lastptr=prev
        firstptr=head
        while firstptr and lastptr:
            temp1=firstptr.next
            temp2=lastptr.next
            firstptr.next=lastptr
            lastptr.next=temp1
            firstptr=temp1
            lastptr=temp2


        