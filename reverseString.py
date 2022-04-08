def reverseString(s=['h', 'e', 'l', 'l', 'o']):
    mid = len(s) // 2
    for i in range(mid):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

    return s

s = ['H', 'a', 'n', 'n', 'a', 'h']
print(reverseString())