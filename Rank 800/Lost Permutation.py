def main():
    _ = int(input())
    for t in range(_):
        m ,s = map(int ,input().split())
        a = list(map(int ,input().split()))
        array = [False ] *1050
        max =a[0]
        continued =True
        for l in a:
            if l> max:
                max = l

            if array[l] == True:
                continued = False
                break

            else:
                array[l] = True
        if not continued:
            print('NO')
            continue
        i = 0
        summ = 0
        while True:
            if summ > s:
                print('NO')
                break
            if summ == s:
                if i >= max:
                    print('Yes')
                    break
                else:
                    b = i
                    while b < max:
                        if array[b] == False:
                            print('NO')
                            continued = False
                            break
                        b += 1
                    if not continued:
                        break
                    else:
                        print('YES')
                        break
            if array[i] == False:
                summ += i
            i += 1


main()

