def main():
    t = int(input())
    for k in range(t):
        s = input()
        n = len(s)
        ans='NO'
        for i in range(n//2-1):
            if s[i]!=s[i+1]:
                ans='YES'
                break
        print(ans)
main()