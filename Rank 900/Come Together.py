def main():
    t = int(input())
    for _ in range(t):
        ar,ac=map(int,input().split())
        br,bc=map(int,input().split())
        cr,cc=map(int,input().split())
        ans=1
        if ac==bc==cc:
            if br == cr == ar:
                ans=1
            elif (br <= ar and cr <= ar) or (br >= ar and cr >= ar):
                ans = min(abs(ac - bc), abs(ac - cc)) + 1
            else:
                ans=1
        if br==cr==ar:
            if cc==ac==bc:
                ans=1

            elif (bc <= ac and cc <= ac) or (bc >= ac and cc >= ac):
                ans=min(abs(ac-bc),abs(ac-cc))+1

            else:
                ans=1
        elif (br>ar and cr<ar) or (br<ar and cr>ar):
            if (bc < ac and cc< ac) or (bc > ac and cc>ac):
                ans= min(abs(ac-bc),abs(ac-cc))+1
            else:
                ans=1

        elif (br > ar and cr > ar) or (br < ar and cr < ar):
            if bc==cc:
                ans = min(abs(ac - bc), abs(ac - cc))
                ans += min(abs(ar - br), abs(ar - cr)) + 1
            elif (bc < ac and cc< ac) or (bc > ac and cc>ac):
                ans= min(abs(ac-bc),abs(ac-cc))
                ans+= min(abs(ar-br),abs(ar-cr))+1
            else:
                ans = min(abs(ar - br), abs(ar - cr)) + 1
        elif br==ar or cr==ar:
            if bc == cc:
                ans = min(abs(ac - bc), abs(ac - cc)) + 1
            elif (bc < ac and cc< ac) or (bc > ac and cc>ac):
                ans = min(abs(ac - bc), abs(ac - cc)) + 1
            else:
                ans=1


        print(ans)
main()


