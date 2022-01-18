class Solution:
    def fib(self, n: int) -> int:
        a=[0,1]
        for i in range(0,n):
            a.append(a[i]+a[i+1])
        return a[n]