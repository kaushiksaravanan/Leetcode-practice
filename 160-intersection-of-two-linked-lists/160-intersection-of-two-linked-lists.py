# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d={}
        t1=headA
        t2=headB
        l1=0
        l2=0
        while t2:
            l2+=1
            t2=t2.next
        while t1:
            l1+=1
            t1=t1.next
        print(l1,l2)
        if l1>l2:
            for i in range(l1-l2):
                headA=headA.next
        if l1<l2:
            for i in range(l2-l1):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        
        return None
        