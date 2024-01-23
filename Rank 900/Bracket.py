def Bracket_permutation(string,n,index,open,close):
    if index == n*2:
        print(string)
        return
    if open < n:
        Bracket_permutation(string+'(',n,index+1,open+1,close)
    if open > close:
        Bracket_permutation(string+')',n,index+1,open,close+1)


def main():
    n = int(input())
    s=''
    Bracket_permutation(s,n,0,0,0)

main()
