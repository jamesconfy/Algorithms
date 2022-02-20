def linearSearch(arr, val=0):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return i + 1

    return -1


a = [1, 3, 4, 5, 6, 7, 11, 12, 23, 34, 51, 53, 55, 61, 70, 72]
val = 74
print(linearSearch(a, val))