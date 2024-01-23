def find_sum(sum,l,r,k,n):
    s=0
    if l==1 and n==r:
        s=n*k
    elif l==1:
        s = sum[-1]-sum[r-1]+(k*(r-l+1))
    elif r==n:
        s=sum[l-2]+(k*(r-l+1))
    elif l==n:
        if l==1:
            s=sum - sum[0] + (k*(n-1))
        elif l==n:
            s=k+sum[-2]
        else:
            s=sum[-1] - s[l-1] + k
    else:
        s=sum[l-2]+sum[-1]-sum[r-1]+(k*(r-l+1))
    if s%2==0:
        print('NO')
    else:
        print('YES')
def main():
    t = int(input())
    for _ in range(t):
        n,q=map(int,input().split())
        array = list(map(int,input().split()))
        summ = [0]*n
        summ[0]=array[0]
        for i in range(1,n):
            summ[i] = array[i]+summ[i-1]
        for i in range(q):
            l,r,k=map(int,input().split())
            find_sum(summ,l,r,k,n)
main()