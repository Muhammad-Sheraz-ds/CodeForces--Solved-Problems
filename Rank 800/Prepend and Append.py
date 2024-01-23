def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        if n == 1:
            print(1)
        else:
            top = 0
            end=n-1
            ans=0
            while end >= top:
                if s[top]==s[end]:
                    ans=(end-top)+1
                    break
                top+=1
                end-=1
            print(ans)
main()