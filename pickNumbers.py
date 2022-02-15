def pickNumbers(arr):
    arr.sort()
    maxCount = 0
    key = arr[0]
    i = 0 
    for i in range(len(arr)):
        count = 0
        for j in range(1+i, len(arr)):
            if abs(arr[i] - arr[j]) <= 1:
                count += 1

        if maxCount < count:
            maxCount = count

    return maxCount + 1
arr = [1, 2, 2, 3, 1, 2]
print(pickNumbers(arr))