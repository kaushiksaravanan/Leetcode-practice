class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        visited=set()
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited:
                    for x in range(1,n):
                        if i+x<n and x+j<m:
                            visited.add((i+x,x+j))
                            if matrix[i][j]!=matrix[i+x][x+j]:
                                return False
        return True
        