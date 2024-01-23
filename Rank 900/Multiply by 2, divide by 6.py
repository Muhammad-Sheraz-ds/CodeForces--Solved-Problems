def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        step=0
        if n == 1:
            print(0)
            continue
        while True:
            if n == 1:
                break
            if n % 6 == 0 or n % 3==0:
                if n % 6 == 0:
                    n = n // 6
                elif n % 3 == 0:
                    n*=2
                step += 1
            else:
                step=-1
                break
        print(step)
main()