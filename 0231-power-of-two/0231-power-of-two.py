class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        while n>0:
            if c>1:
                return False
            k=n&1
            if k==1:
                c+=1
            n=n>>1
        return c==1
        