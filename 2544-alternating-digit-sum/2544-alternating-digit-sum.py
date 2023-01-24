class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        k=1
        for i in str(n):
            s+=int(i)*k
            k*=-1
        return s
        