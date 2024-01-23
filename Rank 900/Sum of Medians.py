def find_index(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n//2-1
    return n//2

def main():
    t = int(input())
    for i in range(t):
        n,k = map(int, input().split())
        array = list(map(int, input().split()))
        index = find_index(n)
        sum=0
        for i in range(index,n * k,n):
            print(i)
            sum+=array[i]
        print(sum)
main()

'''
165
108
145
234
11
3
'''