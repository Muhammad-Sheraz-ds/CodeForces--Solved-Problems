def main():
    t = int(input())
    for i in range(t):
        n1,n2 = map(int,input().split())
        s1 = input()
        s2 = input()
        if n1 < 2 or n2 < 2:
            print('NO')
            continue
        if s1[0]==s1[1] or s2[0]==s2[1]:
            print('NO')
            continue
        s = s1
        for i in range(n2,0,-1):
            s+=s2[i-1]
        count = 0
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]:
                count+=1
                break
        if count==1:
            print('NO')
            continue
        s = s2
        for i in range(n1,0,-1):
            s+=s1[i-1]
        count = 0
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]:
                count+=1
                break
        if count==1:
            print('NO')
        else:
            print('YES')
main()
