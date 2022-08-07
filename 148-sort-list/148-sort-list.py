# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=[]
        t=head
        while t:
            k.append(t.val)
            t=t.next
        k=sorted(k)
        i=0
        t=head
        while t:
            t.val=k[i]
            i+=1
            t=t.next
        return head
            
        