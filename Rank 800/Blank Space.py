def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        i = 0
        max = 0
        while i < n:
            count=0
            while i < n and array[i]==0:
                count+=1
                i+=1
            if count>max:
                max=count
            i+=1

        print(max)
main()
