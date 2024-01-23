def main():
    k = input()
    array = list(map(int,input().split()))
    maxi = max(array)
    d = dict()
    s = set()
    for i in array:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        s.add(i)
    max_count = 0
    max_key = 1
    for i in s:
        if d[i] > max_count:
            max_count = d[i]
            max_key = i
    count = 0
    if max_count == 1:
        n = max(s)
        for j in s:
            if n == j:
                continue
            count += abs(j - n) % 2
    else:
        n = max_key
        for j in s:
            if j == n:
                continue
            count += (abs(j - n) % 2) * d[j]
    print(count)
main()