def main():
    t = int(input())
    for i in range(t):
        inp1_x,inp1_y = map(str,input().split())
        inp2_x,inp2_y = map(str,input().split())
        n1 = inp1_x + '0'* int(inp1_y)
        n2 = inp2_x + '0'* int(inp2_y)
        int(n1)
        int(n2)
        if n1 > n2:
            print('>')
        
        elif n1 < n2:
            print('<')

        elif n1 == n2:
            print('=')

main()
