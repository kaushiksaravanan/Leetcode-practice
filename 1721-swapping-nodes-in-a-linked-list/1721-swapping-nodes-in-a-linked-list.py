# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        i=1
        while(temp):
            if(i==k):
                break
            temp=temp.next
            i+=1
        temph=head
        i=1
        l=1
        while(temph):
            temph=temph.next
            l+=1
        tempw=head
        i=1
        while(tempw):
            if(i==l-k):
                break
            tempw=tempw.next
            i+=1
        print(tempw.val,temp.val)
        t=tempw.val
        tempw.val=temp.val
        temp.val=t
        return head
        