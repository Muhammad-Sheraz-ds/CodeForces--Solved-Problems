def main():
    t = int(input())
    for _ in range(t):
        s=input()
        n=len(s)
        if n <= 10:
            print(s)
        else:
            print(s[0]+str(n-2)+s[-1])
main()