def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n==1:
            print(0)
            continue
        i=0
        while i < 10:
            if 10**i==n:
                print(0)
                break
            elif 10**i > n:
                print(n-(10**(i-1)))
                break
            i+=1


main()