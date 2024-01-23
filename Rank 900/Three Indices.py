def main():
    t= int(input())
    for _ in range(t):
        n= int(input())
        array = list(map(int,input().split()))
        check=[False,False,False]
        i,j,k=0,-1,-1
        ans = 'NO'
        index=0
        check[0]==True
        while True:
            if i < j < k and check[0]==check[1]==check[2]==True:
                ans='Yes'
                break
            if index>=n:
                ans='NO'
                break
            if array[index] < array[i] and check[1]!=True:
                i=index
                check[0]=True
            elif array[index] > array[i]:
                if check[1]==True:
                    if array[index]<array[j]:
                        ans='Yes'
                        k=index
                        check[2]=True
                        break
                    else:
                        j=index

                else:
                    j=index
                    check[1] = True
            elif check[1]==True:
                if array[index] < array[j]:
                    ans = 'Yes'
                    k = index
                    check[2] = True
                    break

            index+=1
        print(ans)
        if ans=='Yes':
            #print(array[i],array[j],array[k])
            print(i+1,j+1,k+1)

main()