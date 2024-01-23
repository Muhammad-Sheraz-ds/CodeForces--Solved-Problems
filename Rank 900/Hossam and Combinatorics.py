def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        d = dict()
        s = set()
        for j in array:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
            s.add(j)

        absolute_difference = max(d) - min(d)
        count = 0
        for j in s:
            for k in s:
                if j == k:
                    continue
                if abs(j - k) == absolute_difference:
                    count+=d[j]

        print(count)







main()
