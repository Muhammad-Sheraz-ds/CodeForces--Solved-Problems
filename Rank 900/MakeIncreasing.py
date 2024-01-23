def is_sorted(list):
    for i in range(len(list)-1):
        if list[i]>=list[i+1]:
            return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        if array[0]!=1 and 1 in array:
            print(-1)
            continue
        if len(array) == 1:
            print(-1)
            continue

        count = 0
        j = 1
        while j < n-1 and is_sorted(array)==False:
            if array[j] > array[j+1]:
                array[j] //= 2
                count+=1
                if array[j-1] > array[j]:
                    while array[j-1]>array[j]:
                        array[j-1] //= 2
                        count+=1

            j+=1
        print(count)

main()