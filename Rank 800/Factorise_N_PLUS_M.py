def is_prime(number):
    if number == 2: return True
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def prime_numbers():
    array = []
    for i in range(2,10000):
        if is_prime(i):
            array.append(i)
    return array

def Factorise_N_PLUS_M():
    t = int(input())
    prime_nos = prime_numbers()
    for i in range(t):
        n = int(input())
        for m in prime_nos:
            if is_prime(n + m)==False and n != m:
                print(m)
                break

Factorise_N_PLUS_M()