def luckyArr(arr):
    result = []
    myset = set(arr)
    for val in myset:
        test = arr.count(val)
        if test == val:
            result.append(val)

    return max(result) if result else -1

print(luckyArr([1, 1, 2, 3, 3]))