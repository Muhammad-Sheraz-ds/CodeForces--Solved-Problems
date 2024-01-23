def equal(array,string):
    for i in range(len(array)):
        if array[i] != string[i]:
            return False
        return True
def PreviousIndex(array,index):
    same_index = index
    i = 0
    while i < index:
        if array[i] == array[index]:
            same_index=i
        i+=1
    return same_index


def NumberReplacement():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        string = input()
        stop = False
        for i in range(n):
            for j in range(i+1,n):
                if string[j] == string[i] and array[i] != array[j]:
                    print('NO')
                    stop = True
                    break
        if stop:
            break
        print('YES')



NumberReplacement()

        