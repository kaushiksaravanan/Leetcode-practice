class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        dist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i,v in enumerate(s):
            d[v]=i
        print(d)
        # s=s.lower()
        for i in range(len(s)):
            if d[s[i]]!=i:
                dist[ord(s[i])-97]=d[s[i]]-i-1
                if d[s[i]]-i-1!=distance[ord(s[i])-97]:
                    return False
        
        print(dist)
        return True
                
            
        