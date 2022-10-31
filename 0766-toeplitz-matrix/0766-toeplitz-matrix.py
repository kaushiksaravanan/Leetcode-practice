class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d={}
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] not in d:
                    for ii in range(n+1000):
                        try:
                            if matrix[i][j]!=matrix[i+ii][j+ii]:
                                d[matrix[i+ii][j+ii]]=1
                                return False
                        except:
                            break
        return True
                            
                    # d[matrix[i][j]]=1
                    