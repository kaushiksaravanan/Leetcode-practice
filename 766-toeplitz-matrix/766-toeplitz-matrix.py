class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        visited={}
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited:
                    for x in range(1,n):
                        if i+x<n and x+j<m:
                            if matrix[i][j]!=matrix[i+x][x+j]:
                                return False
        return True
        