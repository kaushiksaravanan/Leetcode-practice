class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s=s.split(":")
        alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans=[]
        for i in alp[alp.index(s[0][0]):alp.index(s[1][0])+1]:
            for j in range(int(s[0][1]),int(s[1][1])+1):
                ans.append(i+str(j))
        return ans
                
                
        