def lengthOfLongestSubstring(s):
    str = set()
    for i in s:
        str.add(i)
    s=''
    l =0
    for j in str:
        s+=j
        l+=1

    print(f'The answer is {s}, with the length of',{l})

