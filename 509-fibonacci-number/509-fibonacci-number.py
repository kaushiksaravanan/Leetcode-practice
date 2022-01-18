a={}
def fb(n):
    if n not in a:
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            a[n]=fb(n-2)+fb(n-1)
    return a[n]

class Solution:
    def fib(self, n: int) -> int:
        a=[0,1]
        for i in range(0,n):
            a.append(a[i]+a[i+1])
        return a[n]