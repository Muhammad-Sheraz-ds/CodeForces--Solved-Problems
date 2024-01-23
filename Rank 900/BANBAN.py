from
from random import randint
def BANBAN():
    t = int(input())
    for i in range(t):
        n = int(input())
        count=0
        while True:
            if n ==1:
                print(1)
                break
            if 2 ** count > n:
                print(count-1)
                break
            count+=1


BANBAN()