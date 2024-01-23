def main():
    t = int(input())
    for i in range(t):
        n,k = map(int,input().split())
        array = []
        for i in range(n):
            array.append(list(map(int,input().split())))
        for i in range(k):
            p = 0
            m = 0
            for j in range(n):

main()