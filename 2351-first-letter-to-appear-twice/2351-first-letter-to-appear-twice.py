class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                return i
            if i not in d:
                d[i]=1
        