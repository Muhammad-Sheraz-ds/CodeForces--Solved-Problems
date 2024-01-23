def main():
    t = int(input())
    for i in range(t):
        s = input()
        n = len(s)
        if n % 2==1:
            print('NO')
            continue
        cont = True
        start = 0
        middle = n//2
        while start < n//2 and middle< n:
            if s[start] != s[middle]:
                print('NO')
                cont = False
                break
            start+=1
            middle += 1
        if cont:
            print('YES')


main()
