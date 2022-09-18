# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], v: int) -> Optional[ListNode]:
        x=head
        val=[]
        while x:
            if x.val!=v:
                val.append(x.val)
            x=x.next
        print(val)
        x=head
        y=head
        l=0
        print(val)
        if len(val)==0:
            return None
        while x:
            if l>=len(val):
                break
            x.val=val[l]
            y=x
            x=x.next
            l+=1
        try:
            y.next=None
        except:
            y=None
        # print(x.val)
        # x.next=None
        return head
        