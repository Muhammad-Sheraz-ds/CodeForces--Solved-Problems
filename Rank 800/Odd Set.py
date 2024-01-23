def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        o=0
        e=0
        for i in array:
            if i % 2==0:
                e+=1
            else:
                o+=1
        if o==e:
            print('YES')
        else:
            print('NO')

main()