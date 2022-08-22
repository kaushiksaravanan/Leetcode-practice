class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        l=0
        if n<=0:
            return False
        if n==4:
            return True
        while n>1:
            print(n,n%4)
            k=n%4
            if k!=0:
                return False
            n=n//4
            l+=1
        return True