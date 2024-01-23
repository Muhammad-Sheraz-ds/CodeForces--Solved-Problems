def Sum():
    t = int(input())
    for i in range(t):
        x,y,z = map(int,input().split())
        if x == y + z or y == x + z or z == x + y:
            print("YES")
        else:
            print("NO")
Sum()