def Password():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        password_digit = [0,1,2,3,4,5,6,7,8,9]
        for i in array:
            if i in password_digit:
                password_digit.remove(i)
        sum = 0
        combinations = 6
        for i in range(len(password_digit)-1,0,-1):
            sum += combinations * i
        print(sum)

Password()