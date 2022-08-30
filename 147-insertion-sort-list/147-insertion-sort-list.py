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
        for i in range(1, len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j] :
                    arr[j+1]=arr[j]
                    j-=1
            arr[j+1]=key
        print(arr)
        c=head
        i=0
        while c:
            c.val=arr[i]
            i+=1
            c=c.next
        return head