from random import randint

def Increasing():
    t = int(input())
    for i in range(t):
        size = int(input())
        is_increasing = 'YES'
        array = list(map(int,input().split()))
        for i in range(len(array)-1):
            if array[i] in array[i+1:len(array)]:
                is_increasing = 'NO'
        print(is_increasing)

Increasing()