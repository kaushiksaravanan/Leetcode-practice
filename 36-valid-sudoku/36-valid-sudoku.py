class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            d1=set()
            for j in i:
                if j!='.':
                    if j in d1:
                        print(d1,j)
                        return False
                    if j not in d1:
                        d1.add(j)
            d1.clear()
        m=0
        for i in range(len(board)):
            d1=set()
            for j in range(len(board)):
                if board[j][i]!='.':
                    if board[j][i] in d1:
                        return False
                    if board[j][i] not in d1:
                        d1.add(board[j][i])
            d1.clear()

        n=len(board)
        for i in range(0,9,3):
            for j in range(0,9,3):
                d=set()
                for ind_i in range(i,i+3):
                    for ind_j in range(j,j+3):
                        if board[ind_i][ind_j]!='.':
                            if board[ind_i][ind_j] in d:
                                return False
                            if board[ind_i][ind_j] not in d:
                                d.add(board[ind_i][ind_j])
                d.clear()
        return True