# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reve(head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            head = prev
        return head
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=1
        x=head
        flag_l=0
        flag_r=0
        le=[]
        mid=[]
        r=[]
        while x:
            if l>=left and l<=right:
                mid.append(x.val)
            elif l<left:
                le.append(x.val)
            elif l>right:
                r.append(x.val)
            # m.append(x.val)
            x=x.next
            l+=1
        # i=1
        x=head
        
        for i in le+mid[::-1]+r:
            x.val=i
            x=x.next
        # print(lef+mid[::-1]+rig)
        return head
                