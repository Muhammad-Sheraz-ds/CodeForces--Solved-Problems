from random import randint

def team():
    t = randint(1, 10)
    print(f't: {t}')
    count = 0
    for i in range(t):
        x = randint(0,1)
        y = randint(0,1)
        z = randint(0,1)
        print(x,y,z)
        if (x==1 and y==1) or (x==1 and z==1) or (y==1 and z==1):
            count=count+1
    print(count)

team()
