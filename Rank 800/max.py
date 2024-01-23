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
        while i <= n and total_steps<k:
            if n-i<k and step==0:
                k==i
                while k<n:
                    if a[k]==1:
                        max=1
                    k+=1
                start=n-1
                a[start]==max
                break
            elif total_steps<k:
                if a[i]==1:
                    max=1
            if (i+1)%k==0:
                start=i-1
                i=i-1
                total_steps+=1
                step=0
            i+=1
            start+=1





        if start==n-1:
            if a[start]==1:
                print('Yes')
            else:
                print('N0')
        else:
            print('N0')


main()