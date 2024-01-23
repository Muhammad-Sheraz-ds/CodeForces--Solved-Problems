
def main():
    t = int(input())
    for k in range(t):
        n = int(input())
        s = input()
        ans='NO'
        string = 'FBFFBFFBFBFFBFFBFBFFBFFB'
        start = 0
        i = 0
        while i < 24:
            if string[i] == s[start]:
                start+=1
            else:
                start = 0
            i=i+1
            if start==n:
                ans='YES'
                break
        print(ans)



main()


'''def main():
    t = int(input())
    for k in range(t):
        n = int(input())
        s = input()
        ans='YES'
        cur_no = 5
        if s[0]=='F':
            cur_no = 3
        i=0
        while i < n:
            if cur_no % 3 == 0 and cur_no % 5 == 0:
                if i+1 == n or s[i]+s[i+1]!='FB':
                    ans = 'NO'
                    break
                i+=2
            elif cur_no % 3 == 0:
                if s[i]!='F':
                    ans='NO'
                    break

                i+=1

            elif cur_no % 5 == 0:
                if s[i]!='B':
                    ans='NO'
                    break
                i += 1
            cur_no+=1
            while True:
                if cur_no % 3 == 0 or cur_no % 5 == 0:
                    break
                cur_no+=1

        print(ans)

main()
'''