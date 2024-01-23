def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        a = [0]*n
        c = 0
        for j in range(n-1,-1,-1):
            if c < array[j]:
                c=array[j]
            if c!=0:
                a[j]=1
                c-=1
        for v in a:
            print(v,end=' ')
        print()


            
main()


