class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        for i,v in enumerate(s):
            d[v]=i
        for i in range(len(s)):
            if d[s[i]]!=i:
                if d[s[i]]-i-1!=distance[ord(s[i])-97]:
                    return False
        return True
                
            
        