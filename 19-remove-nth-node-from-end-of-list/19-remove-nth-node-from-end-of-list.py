# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m=0
        x=head
        while x:
            x=x.next
            m+=1
        x=head
        m-=1
        if m+1==n:
            return head.next
        while x:
            if m<=n:
                break
            x=x.next
            m-=1
        print(x.val)
        try:
            x.next=x.next.next
        except:
            return None
        return head
        
        