class NQueens:
    def __init__(self,n):
        self.board = [['.']*n for _ in range(n)]
        self.count = 0

    def isSafe(self, row, col):
        # vertically up
        i, j = row-1,col
        while(i>=0):
            if self.board[i][j]=='Q':
                return False
            i-=1

        # diagonal left up
        i, j = row-1,col-1
        while(i>=0 and j>=0):
            if self.board[i][j]=='Q':
                return False
            i-=1
            j-=1

        # diagonal right up
        i, j = row-1,col+1
        while(i>=0 and j<len(self.board)):
            if self.board[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True

    def NQueensSol(self, row):
        if row == len(self.board):
            self.count+=1
            self.print_board()
            return
        for j in range(len(self.board)):
            if self.isSafe(row,j):
                self.board[row][j] = 'Q'
                self.NQueensSol(row+1)
                self.board[row][j] = '.'

    def print_board(self):
            print("---Chess Board---")
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    print(self.board[i][j], end=" ")
                print()


n = int(input("Number of Queens? "))
nq = NQueens(n)
nq.NQueensSol(0)
print("Total Solutions: ",nq.count)