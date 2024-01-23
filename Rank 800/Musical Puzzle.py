def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        st = set()
        for j in range(n-1):
            st.add(s[j]+s[j+1])
        print(len(st))
main()