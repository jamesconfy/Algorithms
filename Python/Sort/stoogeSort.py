def stoogeSort(arr, start, end):
    while start < end:
        if arr[start]  > arr[end]:
            arr[end], arr[start] = arr[start], arr[end]

        start += 1

    return arr

    
def stooge(arr):
    n = len(arr) - 1

    n1 = n//3 * 2

    arr = stoogeSort(arr, 0, n1)
    arr = stoogeSort(arr, n1, n)
    arr = stoogeSort(arr, 0, n1)


arr = [2, 4, 3, 3, 1, 6, 7, 2]
print(stooge(arr))
