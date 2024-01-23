def count_even_odd(count):
    if 
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        odd=0
        even=0
        for i in range(n):
            if array[i]%2==0:
                even+=1
            else:
                odd+=1
        if odd < even:
            count_even_odd(odd)
        elif odd > even:
            count_even_odd(even)

