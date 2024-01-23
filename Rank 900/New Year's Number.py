def main():
    t = int(input())
    for i in range(1,t):
        n = i
        if n== 1901 or n==1902:
            print('Yes')
            continue
        if n < 2020:
            print('NO')
            continue
        ans='YES'
        while True:

            if n < 2020:
                ans='NO'
                break
            if n % 2020== 0 or n % 2021== 0:
                ans='YES'
                break
            elif (n - 2021)%2020==0:
                n-=2021
            elif (n - 2020)%2021==0:
                n-=2020
            else:
                ans='No'
                break
        print(ans)

main()



