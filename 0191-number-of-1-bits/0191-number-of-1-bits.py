class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n>0:
            k=n&1
            if k==1:
                c+=1
            n=n>>1
        return c
        