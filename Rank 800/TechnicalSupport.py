def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        m = input()
        count = 0
        for i in m:
            if i == 'Q':
                count +=1
            elif i == 'A' and count>0:
                count -=1
        if count == 0:
            print('Yes')
        else:
            print('No')

main()