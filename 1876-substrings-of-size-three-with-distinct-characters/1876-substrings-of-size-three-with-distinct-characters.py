class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)-2):
            k=s[i:i+3]
            print(k)
            if len(set(k))==3:
                c+=1
        return c
        