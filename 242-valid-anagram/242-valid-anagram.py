class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k1=list(s)
        k2=list(t)
        k1.sort()
        k2.sort()
        print(k1,k2,k1==k2)
        return k1==k2
        