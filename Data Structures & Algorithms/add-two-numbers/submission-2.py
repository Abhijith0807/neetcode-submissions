# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        temp=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            tempNode=ListNode()
            tempNode.val=(val1+val2+carry)%10
            carry=(val1+val2+carry)//10
            temp.next=tempNode
            temp=tempNode
            if l1:
                l1=l1.next
            else:
                l1= None
            if l2:
                l2=l2.next
            else:
                l2=None
        return(dummy.next)