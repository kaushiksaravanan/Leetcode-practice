# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        c=head
        while c:
            arr.append(c.val)
            c=c.next
        arr.sort()
        c=head
        i=0
        while c:
            c.val=arr[i]
            i+=1
            c=c.next
        return head