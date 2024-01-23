def sum(n):
    s = 0
    for i in str(n):
        s+=int(i)
    return s
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        j = 0
        ans = -1
        while j < 100:
            if sum(j)  == n:
                ans = j
                break
            j+=1

        print(ans)
print(main())