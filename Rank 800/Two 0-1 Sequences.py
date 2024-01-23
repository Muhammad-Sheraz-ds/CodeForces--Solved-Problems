def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        a_ = input()
        b_=input()
        a=[]
        b=[]
        if m>n:
            print('NO')
            continue
        st=0
        while st <n:
            a.append(int(a_[st]))
            if st<m:
                b.append(int(b_[st]))
            st+=1

        ans='NO'
        i=1
        j=0
        l=n
        while i < l:
            if j >= m:
                ans='YES'
                break
            if b[j]==0:
                a[i] = min(a[i],a[i-1])
                n-=1
            else:
                a[i] = max(a[i],a[i-1])
                n -= 1
            if a[i] == b[j]:
                j += 1

            i+=1
        if j >= m:
            ans = 'YES'
        print(ans)
main()
