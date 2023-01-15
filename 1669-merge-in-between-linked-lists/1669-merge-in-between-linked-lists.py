# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n=0
        x=list1
        y=list2
        temp=x
        while x:
            if n==a:
                temp.next=y
                while y.next:
                    y=y.next
            if n==b+1:
                y.next=x
                
            n+=1
            temp=x
            x=x.next
        return list1