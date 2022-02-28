class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        k=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                k.append([s1[i],s2[i]])
        if len(k)>2:
            return False
        if len(k)==1:
            return False
        if len(k)==2:
            r1=k[0]
            r2=k[1]
            if r1[0]==r2[1] and r1[1]==r2[0]:
                return True
        if len(k)==0:
            return True
        return False
                