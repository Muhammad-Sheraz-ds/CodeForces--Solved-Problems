def main():
    t = int(input())
    for j in range(t):
        ans = 'NO'
        array  = []
        array.append(list(map(int,input().split())))
        array.append(list(map(int,input().split())))
        for j in range(4):
            if array[0][0] < array[0][1] and array[0][1] < array[1][1]:
                ans = 'YES'
                break
            else:
                a,b,c,d = array[0][0],array[0][1],array[1][0],array[1][1]
                array[0][0],array[0][1],array[1][0],array[1][1]=c,a,b,d



        print(ans)





main()
