# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0;
        i=0;
        while(l1):

            n1+=(10**i)*(l1.val);
            i+=1;
            l1=l1.next;

        n2=0;
        i=0;
        while(l2):

            n1+=(10**i)*(l2.val);
            i+=1;
            l2=l2.next;
        sum=n1+n2;
        y=ListNode()
        if sum==0:
            return ListNode(0)
        x=y
        while sum>0:
            l=sum%10
            print(l)
            m=ListNode(l)
            y.next=m
            y=y.next
            sum=sum//10
        return x.next