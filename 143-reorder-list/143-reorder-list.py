# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l1=[]
        l2=[]
        t1=head
        l=0
        while t1:
            t1=t1.next
            l+=1
        print(l)
        mid=l//2
        if l%2!=0:
            mid+=1
        t1=head
        curr=0
        while t1:
            if curr<mid:
                l1.append(t1.val)
            else:
                l2.append(t1.val)
            curr+=1
            t1=t1.next
        l1=l1[::-1]
        t1=head
        l=0
        while t1:
            if l%2==0:
                if len(l1)!=0:
                    t1.val=l1.pop()
            else:
                if len(l2)!=0:
                    t1.val=l2.pop()
            l+=1
            t1=t1.next