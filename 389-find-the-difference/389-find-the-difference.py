class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        for i in range(min(len(s),len(t))):
            if s[i]!=t[i]:
                if len(s)>len(t):
                    return s[i]
                else:
                    return t[i]
        if len(s)>len(t):
            return s[-1]
        else:
            return t[-1]
            
        
        