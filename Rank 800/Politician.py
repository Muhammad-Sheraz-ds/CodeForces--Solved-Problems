def main():
    t = int(input())
    for _ in range(t):
        a,b,c = map(int,input().split())
        list = [a,b,c]
        if a == b == c:
            print(1,1,1)
            continue
        m = max(a, b, c)
        if a == b==m or b == c==m or c == a==m:
            for i in range(3):
                if list[i] ==m:
                    print(1,end=' ')
                else:
                    print(m+1-list[i],end=' ')
            print()
        else:
            for i in range(3):
                if list[i] == m:
                    print(0, end=' ')
                else:
                    print(m + 1 - list[i],end=' ')
            print()
main()


