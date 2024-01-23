def distance(number,H,hour=24):
    if number < H:
        return (hour - H) + number
    return number - H

def distance_time(h,H,m,M):
    if m < M:
        H += 1
    return f'{distance(h,H)}  {distance(m,M,60)}'


def min(array,index,H):
    min = distance(array[0][index],H)
    min_index = 0
    for i in range(1,len(array)):
        number = array[i][index]
        min_distance = distance(number,H)
        if min_distance<min:
            min = min_distance
            min_index = i
    min_hour = array[min_index][0]


    for i in range(len(array)):
        if min_hour == array[i][0]:
            if array[min_index][1] < array[i][0]:
                min_index = i
    return min_index

def main():
    t = int(input())
    for k in range(t):
        n,H,M = map(int,input().split())
        array = []
        for i in range(n):
            array.append(list(map(int,input().split())))
        min_index = min(array,0,H)
        print(distance_time(array[min_index][0],H,array[min_index][1],M))


main()
