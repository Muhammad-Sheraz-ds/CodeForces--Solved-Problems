def SocialDistance():
    t = int(input())
    for k in range(t):
        n,m = map(int,input().split())
        array = list(map(int,input().split()))
        if m < n:
            print('NO')
            continue
        previous= array[0]
        ans='YES'
        m-=max(array[0],array[-1])+1
        for i in range(1,n):
            m-=max(array[i],array[i-1])+1
            if m < 0:
                ans='NO'
                break
        print(ans)
SocialDistance()