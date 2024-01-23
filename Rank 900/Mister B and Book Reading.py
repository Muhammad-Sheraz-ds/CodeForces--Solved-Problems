def main():
    p,s,max,ds,rr = map(int,input().split())
    days = 1
    speed = s
    total=s
    total=s
    while total<p:
        total-=rr
        speed+=ds
        if speed>max:
            speed = max
        total+=speed
        days+=1
    print(days)
main()


