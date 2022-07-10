# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], ek: int) -> Optional[ListNode]:
        temp=head
        k=[]
        n=0
        while temp:
            k.append(temp.val)
            temp=temp.next
            n+=1
        print(k,n)
        y=[]
        for i in range(0,n,ek):
            y.append(k[i:i+ek][::-1])
        # print(c)
        if len(y[-1])!=ek:
            y=y[:-1]+[y[-1][::-1]]
        x=[]
        for i in y:
            for j in i:
                x.append(j)
        # for i in range(0,len(k)-ek,ek):
        #     try:
        #         for j in k[i:i+ek][::-1]:
        #             y.append(j)
        #     except:
        #         y.append(k[i])
        
        print(y)
        i=0
        c=head
        while c:
            c.val=x[i]
            c=c.next
            i+=1
        return head
            
            