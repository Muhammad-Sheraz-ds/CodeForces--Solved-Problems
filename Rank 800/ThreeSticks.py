def equal_3_lengths(array):
    for i in range(len(array)-1):
        count = 1
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count+=1
        if count>=3:
            return True
    return False

def count(array,elment):
    count = 0
    for i in range(len(array)):
        if array[i] == elment:
            count += 1
    return count

def max_count(array):
    max = count(array,array[0])
    max_no = array[0]
    for i in range(len(array)):
        count_element = count(array,array[0])
        if max < count_element:
            max = count_element
            max_no = array[i]

    return max_no




def ThreeSticks():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        if equal_3_lengths(array)==False:
            max_occure = max_count(array)
            MaxCount = count(array,max_occure)
            count = 0
            while equal_3_lengths(array)==False:



