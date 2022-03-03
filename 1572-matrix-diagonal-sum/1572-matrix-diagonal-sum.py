class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        k=0
        sum=0
        for i in mat:
            sum+=i[k]
            k+=1
        k=0
        for i in mat[::-1]:
            sum+=i[k]
            k+=1
        if k%2!=0:
            return sum-mat[k//2][k//2]
        return sum