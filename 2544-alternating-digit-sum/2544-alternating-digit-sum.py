class Solution:
    def alternateDigitSum(self, n: int) -> int:
        val=[]
        while n>0:
            val.append(n%10)
            n=n//10
        print(val)
        s=0
        k=1
        for i in val[::-1]:
            s+=k*i
            k*=-1
        return s
        
        