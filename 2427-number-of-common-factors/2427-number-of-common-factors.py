class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        val=0
        for i in range(1,min(a,b)+1):
            if a%i==b%i and a%i==0:
                val+=1
        return val