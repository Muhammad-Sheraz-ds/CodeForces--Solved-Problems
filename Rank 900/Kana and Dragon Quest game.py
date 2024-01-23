def main():
    t = int(input())
    for _ in range(t):
        val,n,m = map(int,input().split())
        ans = 'NO'
        c_n,c_m  = 0,0
        while True:
            if val<=0:
                ans='YES'
                break
            if c_n >= n and c_m>=m:
                ans='NO'
                break
            if c_n < n and val>9:
                val = val//2+10
                c_n+=1
            elif c_m<m:
                val-=10
                c_m+=1
        print(ans)



main()