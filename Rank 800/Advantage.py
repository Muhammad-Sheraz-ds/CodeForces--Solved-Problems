def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        max=array[0]
        m_i=0
        m_i_2 = 0
        max_2 = array[0]
        i = 0
        while i < n:
            if array[i]>=max:
                max=array[i]
                m_i = i
            i+=1
        j = 0
        while j < n:
            if m_i == j:
                continue
            if array[j]==max:
                m_i_2=j
                max_2=max
                break
            if array[j]>max_2:
                m_i_2=j
                max_2=array[j]
            j+=1
        for i in range(n):
            if array[i] == max:
                print(array[i]-array[m_i_2],end=' ')
            else:
                print(array[i]-max,end=' ')
        print()


main()