# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=[]
        more=[]
        t=head
        l=0
        while t:
            if t.val<x:
                less.append(t.val)
                l+=1
            else:
                more.append(t.val)
            t=t.next
        i=0
        t=head
        while t:
            if i<l:
                t.val=less[i]
            else:
                t.val=more[i-l]
            t=t.next
            i+=1
        return head
        