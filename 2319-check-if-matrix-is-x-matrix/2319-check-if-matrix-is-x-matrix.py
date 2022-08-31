class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    if i==j:
                        return False
                else:
                    if i+j!=n-1 and i!=j:
                        return False
                if i+j==n-1 and grid[i][j]==0:
                    return False
        return True