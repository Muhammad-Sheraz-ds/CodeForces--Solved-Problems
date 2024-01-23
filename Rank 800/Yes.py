def main():
    t = int(input())
    for i in range(t):
        s = input()
        string = 'Yes'
        ans='Yes'
        if s[0] not in string:
            print('No')
            continue
        start=string.index(s[0])
        for i in s:
            if i not in string:
                ans='No'
                break
            if i!= string[start]:
                ans = 'No'
                break
            start=(start+1)%3
        print(ans)

main()