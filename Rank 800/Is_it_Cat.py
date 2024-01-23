def Is_it_Cat():
    t = int(input())
    for i in range(t):
        n = int(input())
        voice = input()
        if voice[0].lower()!='m':
            print('NO')
            continue
        d = {'e':'m','o':'e','w':'o','w':'w'}
        v =''
        target='meow'
        ans='YES'
        i=0
        for j in range(1,n):
            if i==4:
                break
            if voice[j].lower() == voice[j - 1].lower() or voice[j].lower() == d[voice[j].lower()]:
                pass
                if voice[j].lower()==target[i]:
                    i+=1


        print(ans)



Is_it_Cat()

'''
            if j!=n-1 and voice[j].lower() == voice[j + 1].lower() or voice[j].lower() == d[voice[j].lower()]:
                pass              
            elif voice[j].lower()==voice[j+1].lower() or voice[j].lower()==d[voice[j].lower()]:
                pass

'''