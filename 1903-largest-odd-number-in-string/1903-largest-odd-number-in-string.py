class Solution:
    def largestOddNumber(self, num: str) -> str:
        k='24680'
        l=0
        for i in num[::-1]:
            if i not in k:
                return num[:len(num)-l]
            l+=1
        return ""