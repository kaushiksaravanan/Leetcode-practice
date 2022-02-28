class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        k=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                k.append([s1[i],s2[i]])
        if len(k)==0:
            return True
        if len(k)==2:
            if k[0][0]==k[1][1] and k[0][1]==k[1][0]:
                return True
        return False
                