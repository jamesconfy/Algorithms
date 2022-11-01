def interSearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end and target >= arr[start] and target <= arr[end]:
        mid = start + int(((float(end - start)/(arr[end] - arr[start])) * (target - arr[start])))
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [1, 2, 3,4 ,5,15,7,8,9,10]
arr.sort()
print(interSearch(arr, 15))