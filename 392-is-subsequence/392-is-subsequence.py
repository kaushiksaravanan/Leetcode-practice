class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        if s==t:
            return True
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        try:
            for i in range(len(t)):
                if s[l]==t[i]:
                    l+=1
            return l==len(s)
        except:
            return True