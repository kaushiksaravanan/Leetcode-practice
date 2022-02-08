class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        k=len(num)
        while k!=1:
            s=0
            for i in num:
                s+=int(i)
            num=s
            k=len(str(num))
            num=str(num)
        return num