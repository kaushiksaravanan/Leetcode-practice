class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l=0
        c=0
        for i in s:
            if i==letter:
                c+=1
            l+=1
        print(c/l)
        return floor((c/l)*100)
        