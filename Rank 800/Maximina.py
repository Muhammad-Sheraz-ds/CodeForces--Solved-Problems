def is_1(a,start,end,n):
    for i in range(start,end):
        if a[i]==n:
            return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        i = 1
        start=0
        total_steps = 0
        step=0
        max = 0
        if k==n:
            if is_1(a,0,n,1):
                print("Yes")
            else:
                print('NO')
        else:
            max=0
            end=n-(n//(k-1)-1)
            if is_1(a,0,end,1):
                max=1
            if is_1(a,end+1,n,0):
                max=0
            if max==1:
                print('Yes')
            else:
                print('NO')


main()