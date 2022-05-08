# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        l=0
        while x:
            x=x.next
            l+=1
        if l==1:
            return None
        l=l//2
        l-=1
        i=0
        x=head
        while x:
            if i==l:
                x.next=x.next.next
            x=x.next
            i+=1
        return head