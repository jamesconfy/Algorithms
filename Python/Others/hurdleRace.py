def hurdlerace(arr, k):
    maxHeight = max(arr)
    if k >= maxHeight:
        return 0
    else:
        return abs(maxHeight - k)

arr = [1, 2, 3, 3, 1]
k = 1
print(hurdlerace(arr, k))