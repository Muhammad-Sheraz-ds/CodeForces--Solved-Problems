def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        i = 0
        ans='YES'
        count=1
        while i < n:
            if count %2==0:
                if i+1==n or s[i]!=s[i+1]:
                    ans='NO'
                    break
                i+=2
            else:
                i+=1
            count+=1
        print(ans)
main()