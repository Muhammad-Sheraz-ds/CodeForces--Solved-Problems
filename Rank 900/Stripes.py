def main():
    t = int(input())
    for k in range(t):
        array = []

        b = input()
        for j in range(8):
            array.append(input())

        ans = 'B'
        for i in range(8):
            if array[i] == 'RRRRRRRR':
                ans = 'R'
                break
        print(ans)



main()