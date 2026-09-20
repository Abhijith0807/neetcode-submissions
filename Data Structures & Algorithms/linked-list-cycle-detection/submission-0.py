# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowptr=head
        fastptr=head
        while slowptr and fastptr:
            if not fastptr.next:
                return(False)
            else:
                fastptr=fastptr.next.next
                if slowptr==fastptr:
                    return(True)
            slowptr=slowptr.next
        return(False)

        