from random import randint

def Kevin_Permutation():
    t = randint(1, 10)
    print(f't: {t}')
    for i in range(t):
        size = int(input('Enter size of set: '))
        set = {(randint(1,10),randint(1,10)) for i in range(size)}
        print(set)
        list  = []
        for i in set:
            for j in i:
                list.append(j)
        set = {}
        for in range()

Kevin_Permutation()