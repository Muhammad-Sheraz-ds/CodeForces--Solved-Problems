
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        d= dict()
        for i in s:
            d[i]=False
        index = [None]*n
        index[0]=1
        d[s[0]] = 0
        i = 1
        ans='YES'
        while i < n:
            if type(d[s[i]])==bool:
                index[i] = 1-index[i-1]
                d[s[i]]=i
            else:
                index[i] = index[d[s[i]]]
                d[s[i]] = i
            if index[i-1]==index[i]:
                ans='NO'
                break
            i+=1
        print(ans)
main()
'''            if index[i]==False:
                index[i]=1-previous
                d[s[i]] = i
                previous = index
            else:
    '''