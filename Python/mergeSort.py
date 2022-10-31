def merge(arr, l, m, r):
    # get the sizes of each subarrays
    n1 = m - l + 1
    n2 = r - m

    # making a temp subarrays
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0   # Initial index of first subarray
    j = 0   # Initial index of second subarray
    k = l   # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    # code here
    if l < r:
        m = l + (r - l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

    return arr


arr = [1, 2, 5, 3, 4, 7, 2]
l = 0
r = len(arr) - 1
print(mergeSort(arr, l, r))
