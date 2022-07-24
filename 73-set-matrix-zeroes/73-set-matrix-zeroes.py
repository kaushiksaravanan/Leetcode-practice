class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        d_i={}
        d_j={}
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    d_i[i]=1
                    d_j[j]=1
        for i in range(n):
            for j in range(m):
                if i in d_i:
                    matrix[i][j]=0
                elif j in d_j:
                    matrix[i][j]=0
                
                # if j==0:
                    # j=999
                print(j,end=' ')
            print()
        