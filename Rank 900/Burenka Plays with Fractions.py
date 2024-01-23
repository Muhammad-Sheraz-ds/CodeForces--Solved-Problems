a = [[1,2],[2,3]]
print(a.index([1,2]))
'''def sampleword(word):
    array = ['this','wats','oahs','fgdt']
    i = 0
    j = len(array) - 1
    while i < len(array) and i < len(word):
        if word[i] == array[i][i] or word[i] == array[j][j]:
            i += 1
            j -= 1
        else:
            break
        if i == len(array) or j == -1 or i == len(word):
            return True
    i = len(array) -1
    j = 0
    while i >= 0 and j < len(array) and j < len(word):
        if array[j][i] == word[i] or array[i][j] == word[i]:
            i -= 1
            j += 1
        else:
            break
        if i == -1 or j == len(array) or j == len(word):
            return True
    for i in range(len(array)):
        if array[i] == [word]:
            return True
    for i in range(len(array)):
        k = 0
        for j in range(len(array)):
            if array[j][i] == word[k]:
                k +=1
            else:
                break
            if j == len(array) - 1 and i == len(array) - 1  or (j == len(array) - 1 and i == len(array)):
               return True
    for i in range(0,len(array),1):
        k = 0
        for j in range(len(array)-1,-1,-1):
            if array[j][i] == word[k]:
                k +=1
            else:
                break
            if j == 0 or i == len(array)  or (j == len(array) - 1 and i == len(array)):
               return True
'''


def gcd(n1,n2):
    mini = min(n1,n2)
    diuviser = 1
    for i in range(2,mini+1):
        if n1 % i == 0 and n2 % i == 0:
            diuviser = i
    return diuviser

def main():
    t = int(input())
    for i in range(t):
        a,b,c,d = map(int,input().split())
        if a == 0 and c == 0:
            pass
        elif a == 0 or c == 0:
            print(1)
            continue
        if a / b ==  c / d:
            print(0)
            continue
        div = gcd(a,b)
        a= a / div
        b = b / div
        div = gcd(c,d)
        c = c / div
        d = d / div
        count = 0
        if a != c:
            count += 1
        if b != d:
            count+=1
        print(count)


main()