class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        k=0
        for i in s:
            if i=='R':
                c+=1
            if i=='L':
                c-=1
            if c==0:
                k+=1
        return k
        