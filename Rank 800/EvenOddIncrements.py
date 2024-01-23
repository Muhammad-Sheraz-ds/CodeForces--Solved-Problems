def EvenOddIncrements():
    t = int(input())
    for i in range(t):
        n,q = map(int,input().split())
        array = list(map(int,input().split()))
        for i in range(q):
            q1,q2 = map(int,input().split())
            for i in range(len(array)):
                if array[i] % 2 == 0:
                    array[i] += q2
                else:
                    array[i] += q1
            print(sum(array))

EvenOddIncrements()
