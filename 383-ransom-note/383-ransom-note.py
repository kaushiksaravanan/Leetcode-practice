class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            if i not in d:
                d[i]=1
            # d[i]=1
        for i in ransomNote:
            if i not in d or d[i]==0:
                return False
            if d[i]>0:
                d[i]-=1
        return True
            
        