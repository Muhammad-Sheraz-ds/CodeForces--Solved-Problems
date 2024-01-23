def main():
    n = int(input())
    s = set(map(int,input().split()))
    if len(s)==1:
        print('NO')
        return
    for k in s:
        g = 0
        for c in s:
            if k < c:
                g+=1
                if g > 1:
                    break
        if g == 1:
            print(k)
            return

main()