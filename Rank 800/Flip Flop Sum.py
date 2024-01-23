def overlay_number(arr, number):
    j = 0
    while number > 0:
        last_bit = number & 1
        if last_bit:
            print(arr[j], end='')
        j += 1
        number = number >> 1
    print()

def generate_all_subsequences(arr):
    n = len(arr)
    for i in range(2**n):
        overlay_number(arr, i)

# Main code
arr = input("Enter a string: ")
generate_all_subsequences(arr)
