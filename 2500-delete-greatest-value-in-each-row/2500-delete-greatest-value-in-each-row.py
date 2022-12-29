class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n=len(grid)
        mm=len(grid[0])
        ans=0
        while max(grid[0])!=-999:
            m=[]
            for i in range(n):
                k=max(grid[i])
                if k!=-999:
                    for j in range(mm):
                        if grid[i][j]==k:
                            grid[i][j]=-999
                            break
                m.append(k)
            ans+=max(m)
            # break
        return ans
                
                    

                
                
        