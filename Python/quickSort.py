# Function to sort a list using quick sort algorithm.
def quickSort(arr, low, high):
    # code here
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

    return arr

def partition(arr, low, high):
    # code here
    pivot = arr[high]
    i = low - 1
    j = low

    while j <= high - 1:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [2, 5, 4, 6, 1, 9, 3]
p1 = 0
p2 = len(arr) - 1
print(quickSort(arr, p1, p2))
