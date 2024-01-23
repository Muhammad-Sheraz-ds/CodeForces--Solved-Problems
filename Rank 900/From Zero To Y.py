def find_P(x,y):
    i= 0
    while i < 10:
        val = x * (10**i)
        if val > y:
            return y-(x * (10**(i-1)))
        elif val == y:
            return 0
        i+=1


def main():
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        step=0
        while y!=0:
            if y < x:
                step+=y
                break
            if y == 1:
                y=0
                step+=1
                break
            y = find_P(x,y)
            step+=1
        print(step)
main()
