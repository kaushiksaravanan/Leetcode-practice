class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s1=0
        s2=0
        f=0
        c=0
        while n>0:
            if f==0:
                s1+=n%10
                f=1
            else:
                s2+=n%10
                f=0
            n=n//10
            c+=1
        if c%2!=0:
            return s1-s2
        return s2-s1
        
        