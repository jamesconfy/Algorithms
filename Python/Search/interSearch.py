def interSearch(arr, target):
    first = 0
    end = len(arr) - 1
    while first <= end and target >= arr[first] and target <= arr[end]:
        mid = first + int(((float(end - first)/(arr[end] - arr[first])) * (target - arr[first])))
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            first = mid + 1
        else:
            end = mid - 1

    return -1


arr = [1, 2, 3,4 ,5,15,7,8,9,10]
arr.sort()
print(interSearch(arr, 15))