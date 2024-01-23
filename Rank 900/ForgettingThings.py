import random
def main():
    a,b = map(int,input().split())
    d = abs(a-b)
    if d == 8:
        if a == 9:
            print(9,' ',10)
        else:
            print(-1)
    elif d > 1:
        print(-1)

    elif d == 1:
        if a > b:
            print(-1)
        else:
            b *=100
            print(b-1,' ',b)
    elif d == 0:
        n = random.randint(11, 98)
        print(f'{a}{n} {b}{n+1}')

main()