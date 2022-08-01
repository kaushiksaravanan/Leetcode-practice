import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        def f(r,c):
            if c==n-1 or r==m-1:
                return 1
            if (r,c) in d:
                return d[(r,c)]
            n1=f(r,c+1)
            n2=f(r+1,c)
            d[(r,c)]=n1+n2
            return d[(r,c)]
        return f(0,0)