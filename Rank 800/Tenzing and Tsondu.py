def main():
    t = int(input())
    for i in range(t):
        tsedu,tenzey = map(int,input().split())
        x = list(map(int,input().split()))
        y = list(map(int,input().split()))
        i = 0
        j=0
        while True:
            if i == tsedu and j == tenzey:
                print('Draw')
                break
            elif i == tsedu:
                print('Tenzing')
                break
            elif j == tenzey:
                print('Tsondu')
                break
            if x[i] - y[j]==0:
                j+=1
                i+=1
            else:
                if y[j] < x[i]:
                    x[i] = x[i] - y[j]
                    j+=1
                else:
                    y[j] = y[j] - x[i]
                    i += 1
main()
