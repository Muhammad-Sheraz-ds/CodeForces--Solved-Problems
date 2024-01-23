'''
There's a chessboard of size n×n. m rooks are placed on it in such a way that:
no two rooks occupy the same cell;
no two rooks attack each other.
A rook attacks all cells that are in its row or column.
Is it possible to move exactly one rook (you can choose which one to move) into a different cell so that no two rooks still attack each other? A rook can move into any cell in its row or column if no other rook stands on its path.

Input

The first line contains a single integer t (1≤t≤2000) — the number of testcases.
The first line of each testcase contains two integers n and m (1≤n,m≤8) — the size of the chessboard and the number of the rooks.
The i-th of the next m lines contains two integers xi and yi (1≤xi,yi≤n) — the position of the i-th rook: xi is the row and yi is the column.
No two rooks occupy the same cell. No two rooks attack each other.

Output

For each testcase, print "YES" if it's possible to move exactly one rook into a different cell so that no two rooks still attack each other. Otherwise, print "NO"
'''
from random import randint
def CowardlyRooks():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        array = [list(map(int,input().split()))]
        print(array)
        rock1 = 0
        rock2 = 0
        for i in range(m):
            a = randint(0, len(array)-1)
            b = randint(0, len(array)-1)
            n = 2
            if array[a][b] != 2:
                array[a][b] == 2
            else:
                while array[a][b]==2:
                    a = randint(0, len(array)-1)
                    b = randint(0, len(array)-1)
                    if array[a][b] != 2:
                        array[a][b] == 2

        x = randint(0,len(array)-1)
        y = randint(0, len(array)-1)
        while  array[x][y] != 2:
            x = randint(0, len(array)-1)
            y = randint(0, len(array)-1)
            array[x][y] == 2
            break
        is_attack =True
        for row in range(x,len(array)-1):
            for col in range(y,len(array)-1):
                if array[row][col]==2 or array[col][row]==2:
                    is_attack==False
        if is_attack:
            for row in range(len(array)-1,x,-1):
                for col in range(len(array)-1,y,-1):
                    if array[row][col] == 2 or array[col][row] == 2:
                        ('No')
                return 'yes'
        return 'No'



def main():
    print(CowardlyRooks())

main()
