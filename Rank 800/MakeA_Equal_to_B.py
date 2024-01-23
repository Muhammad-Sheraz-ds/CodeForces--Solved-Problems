def MakeA_Equal_to_B():
    t = int(input())
    for i in range(t):
        n = int(input())
        array1 = list(map(int,input().split()))
        array2 = list(map(int,input().split()))
        if array1==array2:
            print(0)
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                array1[i] = 1 - array1[i]
        if array1==array2:
            print(1)
        else:
            print(2)

MakeA_Equal_to_B()