def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n ==6 or n == 4:
            print(1,' ',1)
        elif n % 6 == 0 or n % 4 == 0:
            print(n//6,' ',n//4)
        else:
            print(-1)

main()