def main():
    t = int(input())
    for i in range(t):
        s = input()
        cf = 'codeforces'
        c = 0
        for i in range(10):
            if s[i]!=cf[i]:
                c+=1
        print(c)

main()