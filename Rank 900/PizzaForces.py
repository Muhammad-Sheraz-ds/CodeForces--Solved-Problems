def give_sum(n,d,m):
    s = n//d*m
    r = n%d
    if r==0:
        return s
    elif r <=6:
        return s+15
    elif r <=8:
        return s+20
    elif r <=10:
        return s+25


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n <= 6:
            print(15)
        elif n <= 8:
            print(20)
        elif n <= 10:
            print(25)
        else:
            a=give_sum(n,10,25)
            b=give_sum(n,8,20)
            c=give_sum(n,6,15)
            print(min(a,b,c))


main()

'''
        elif n%10==6:
            print((n//10)*25+15)
        elif n%10==8:
            print((n//10)*25+20)
        elif n%8==6:
            print((n//8)*20+15)
        elif n % 10 == 0 or n%6==0 or n%8==0:
            print(int(2.5*n))
            continue



        else:
            i = n
            while i < n+10:
                if i % 6 == 0:
                    print(int((i//6)*15))
                    #print(int((n//6)*2.5)+15)
                    break
                elif i % 8 == 0:
                    print(int((i//8)*20))
                    break
                elif i % 10 == 0:
                    print(int((i//10)*25))
                    break
                i+=1

'''