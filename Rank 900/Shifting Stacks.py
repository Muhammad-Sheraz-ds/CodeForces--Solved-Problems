def main():
    t = int(input())
    for k in range(t):
        l = int(input())
        array = list(map(int,input().split()))
        ans = 'YES'
        if l == 1:
            print('YES')

        elif l == 2:
            if array[0] == 0 and array[1]==0:
                print('NO')
            else:
                print('YES')

        else:
            count0 = 0
            count1 = 0
            if array[0] == 0:
                count0+=1
            if array[0]==0:
                count1+=1
            ans = 'YES'
            for i in range(1,l):


                if array[i] == 0:
                    count0 += 1
                if array[i] == 1:
                    count1 += 1
                if count0 > 1 or count1 > 1:
                    print('NO')
                    break

                while array[i] <= array[i-1]:
                    n = abs(array[i]-array[i-1]) + 1
                    array[i]+=n
                    j =i
                    while j > 0:
                        if array[j-1] - n <  0:
                            count0+=1
                            break
                        else:
                            array[j - 1] -= n
                        j-=1
            print(ans)
main()

'''else:
            count0 = 0
            count1 = 0
            for i in range(0,l):
                if array[i] == 0:
                    count0+=1
                if array[i] == 1:
                    count1+=1
                if count0>1 or count1>1:
                    print('NO')
                    break
                j = i
                while j > 0 and array[j] <= array[j-1]:
                    array[j]+=1
                    if array[j-1]==0:
                        count0+=1
                        print('NO')
                    else:
                        array[j-1] -= 1
                    j-=1'''



'''if array[i] <= array[i-1]:
                    while array[i] <= array[i-1]:
                        if array[i-1] == 0:
                            ans = 'NO'
                            break
                        else:
                            array[i]+=1
                            array[i-1]-=1
        print(ans)

main()

'''

