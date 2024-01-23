def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        i = 0
        start=0
        total_steps = 0
        step=0
        max = 0
        while i <= n:
            if step == k:
                total_steps+=1
                step=0
                start=total_steps*k
                a[start]=max
            if total_steps >= k:
                break
            if  start-n<k+1 and i%k==0 and  total_steps<k:
                if (k - total_steps+1)*3>n-step:
                    m=i-1
                    while m <  n:
                        if a[m]==0:
                            max=0
                        m+=1
                    start=n-1
                    a[start] = max
                    break
                else:
                    start=n-1
                    a[start] = 0
                    break
            elif a[i-1]==1:
                max=1
            step += 1
            i+=1

        if start==n-1:
            if a[start]==1:
                print('Yes')
            else:
                print('N0')
        else:
            print('N0')


main()