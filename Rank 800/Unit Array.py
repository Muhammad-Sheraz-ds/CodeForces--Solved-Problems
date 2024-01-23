def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        c1 = 0
        c2 =0
        for i in array:
            if i==1:
                c1+=1
            else:
                c2+=1
        if c1 > c2:
            if c1%2==0 or c2%2==0:
                print(1)
            else:
                print(0)
        elif c1 == c2:
            print(0)
        else:
            if c1%2==0 or c2%2==0:
main()
