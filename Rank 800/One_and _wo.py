def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        m= 1
        k = 0
        ans = -1
        while k < n:
            m*=array[k]
            k+=1
        m2 = 1
        k = 0
        while k < n:
            val = array[k]
            m2*=val
            m/=val
            if m==m2:
                ans=k+1
                break
            k+=1
        print(ans)


main()