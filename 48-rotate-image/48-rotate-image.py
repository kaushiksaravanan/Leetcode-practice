class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        k=[]
        for i in [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]:
            k.append(i[::-1])
        matrix[:]=k
        # return k
        