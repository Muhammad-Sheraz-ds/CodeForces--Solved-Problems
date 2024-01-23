def length_L(a,b):
    if len(a) > len(b):
        print('>')
    elif len(a) < len(b):
        print('<')
    else:
        print('=')

def length_S(a,b):
    if len(a) < len(b):
        print('>')
    elif len(a) > len(b):
        print('<')
    else:
        print('=')

def CompareTShirtSizes():
    t = int(input())
    for i in range(t):
        a,b = map(str,input().split())
        if a[-1]  == 'L':
            if b[-1] == 'S' or b[-1] == 'M':
                print('>')
            else:
                length_L(a,b)
        elif a[-1] == 'S':
            if b[-1] == 'L' or b[-1] == 'M':
                print('<')
            else:
                length_S(a, b)
        elif a[-1] == 'M':
            if b[-1] == 'S':
                print('>')
            elif b[-1] == 'L':
                print('<')
            else:
                print('=')

CompareTShirtSizes()