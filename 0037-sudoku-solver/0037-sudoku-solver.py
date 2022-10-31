class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(r,c,num):
            for i in range(9):
                if board[i][c]==str(num):
                    return False
            for i in range(9):
                if board[r][i]==str(num):
                    return False
            sqrt=3
            st=r-r%3
            en=c-c%3
            for i in range(st,st+3):
                for j in range(en,en+3):
                    if board[i][j]==str(num):
                        return False
            return True
        def solve():
            row=-100
            col=-100
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        row=i
                        col=j
                        break
                if row==-100 or col==-100:
                    break
            if row==-100 and col==-100:
                return True
            for fill in range(1,10):
                if check(row,col,fill):
                    board[row][col]=str(fill)
                    m=solve()
                    if m==False:
                        board[row][col]='.'
                    else:
                        return True
            return False
        solve()
                        
                        