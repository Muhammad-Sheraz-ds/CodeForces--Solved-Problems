def main():
    t= int(input())
    for i in range(t):
        n,s= map(int,input().split())
        print(s//(n**2))

main()