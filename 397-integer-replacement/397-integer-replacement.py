d={}
class Solution:
    def integerReplacement(self, n: int) -> int:
        def f(n):
            if n==1:
                return 0
            if n in d:
                return d[n]
            if n%2==0:
                d[n]=1+f(n//2)
                return d[n]
            else:
                n1=1+f(n-1)
                n2=1+f(n+1)
                d[n]=min(n1,n2)
                return d[n]
        return f(n)
        
        '''Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 '''
        