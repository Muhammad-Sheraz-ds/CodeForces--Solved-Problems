def main():
    t = int(input())
    for j in range(t):
        n = input()
        data = input()
        sum = int(data[0])
        ans = ''
        i = 1
        while i < len(data):
            if sum == 1:
                if int(data[i]) == 1:
                    ans += '-'
                    sum = 0
                elif int(data[i]) == 0:
                    ans+='+'
                    sum = 1
            else:
                sum += int(data[i])
                ans+='+'

            i += 1
        print(ans)


main()




