def main():
    t = int(input())
    for _ in range(t):
        array=[]
        ans=''
        for i in range(8):
            s = input()
            array.append(s)
        is_continue=False
        for i in range(8):
            for j in range(8):
                if array[i][j]!='.':
                    m=i
                    while m < 8:
                        if array[m][j]!='.':
                            ans+=array[m][j]
                        m+=1
                    is_continue=True
                    break
            if is_continue:
                break
        print(ans)


main()

