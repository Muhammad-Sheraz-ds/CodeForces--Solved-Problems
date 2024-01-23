def fill(board,n,row,col):
    if row==n or col == n or col < 0 or row < 0: return None
    board[row][col] = 1
    fill(board,n,row,col)
    fill(board,n,row,col)
    fill(board,n,row,col)
    fill(board,n,row,col)
    fill(board,n,row,col)
    fill(board,n,row,col)


def NQueen(board,n,row,col):
    if row == n:
        print(board)
    if row < 0 or col < 0 or col == n:
        return
    if board[row][col] == None:
        board[row][col] = 'Q'
        for i in range()
        NQueen(board,n,row)





def main():
    n = int(input())
    chess = [[None for i in range(n)]for j in range(n)]
    chess = [[False for i in range(n)]for j in range(n)]
    NQueen(board,n,0,0)

main()