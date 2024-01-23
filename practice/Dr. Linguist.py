def main():
    #n = int(input())
    l = input()
    d = dict()
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    s = set()
    for k in d.values():
        s.add(k)
    l = len(s)
    print(s)
    if l > 2:
        print('N0')
    elif l == 1:
        print('YES')
    elif l==2:
        a,b = s
        mn = min(a,b)
        mx = max(a,b)
        c=0
        for k in d.values():
            if k == mx:
                c+=1
        if abs(mn-c)==0:
            print('YES')
        else:
            print('NO')






main()
        