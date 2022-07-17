a=[0]*100000
a[0]=1
a[1]=2
top=2
# a[2]=1
class Solution:
    def climbStairs(self, n: int) -> int:
        # print(a[:10])
        global top
        if a[n]==0:
            for i in range(top,n+1):
                a[i]=a[top-1]+a[top-2]
                top+=1
        # print(a)
        return a[n-1]