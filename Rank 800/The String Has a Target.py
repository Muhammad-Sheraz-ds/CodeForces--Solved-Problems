t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    min=ord(s[0])
    ind =0
    for j in range(1,n):
        if ord(s[j])<min:
            min=ord(s[j])
            ind = j
    target = s[ind]
    for j in range(0, n):
        if j!=ind:
            target+=s[j]
    print(target)




