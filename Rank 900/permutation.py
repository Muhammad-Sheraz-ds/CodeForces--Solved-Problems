

def print_array(array):
    for i in range(len(array)-1):
        print(array[i],end='')
    print()

def permutation(arr,n,index):
    if index >= n:
        return
    j= index
    for i in range(j,n-1):
        arr[j],arr[i]=arr[i],arr[j]
        print_array(arr)
        permutation(arr,n,index+1)
        arr[j],arr[i]=arr[i],arr[j]
def main():
    s = input()
    n = len(s)+1
    array = [None] * n
    for i in range(len(s)):
        array[i]=s[i]
    permutation(array,n,0)

main()
