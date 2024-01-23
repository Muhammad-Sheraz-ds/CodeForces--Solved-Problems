def main():
    t= int(input())
    for _ in range(t):
        a,b,n = map(int,input().split())
        attack = list(map(int,input().split()))
        health = list(map(int,input().split()))
        i = 0
        j=0
        while True:
            if i == n:
                ans = 'YES'
                break
            elif b <= 0:
                ans = 'NO'
                break
            else:
                b -= attack[i]
                health[i] -= a
                attack[i] = 0
                if health[i]<=0:
                    i+=1

        print(ans)


main()




