class Solution:
    def makeGood(self, s: str) -> str:
        # def check(s):
            
        while True:
            f=0
            for i in range(len(s)-1):
                if s[i]!=s[i+1] and( s[i].upper()==s[i+1] or s[i].lower()==s[i+1] or s[i]==s[i+1].upper() or s[i]==s[i+1].lower()):
                    s=s[:i]+s[i+2:]
                    f=1
                    # print(i)
                    break
                    
            if f==0:
                break
        return s
            