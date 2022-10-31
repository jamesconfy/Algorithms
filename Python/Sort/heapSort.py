def Heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[largest] > arr[l]:
       largest = l

    if r < n and arr[largest] > arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        Heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        Heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        Heapify(arr, i, 0)

arr = [3, 12, 11, 4, 11, 0, 1, -100, 13, 5, 6, 7, 2, -1]
heapSort(arr)
print("Sorted array is", arr)