def main():
    n=int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    max = a[0]
    x = [max] * n
    m = max
    for i in range(1,n):
        b[i] = max
        if a[i] > max:
            max = a[i]
        x[i] = a[i] + m
        if m < x[i]:
            m = x[i]

    for v in x:
        print(v,end=' ')
    print()

main()
