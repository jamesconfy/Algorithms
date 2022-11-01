def binarySearch( arr, lo, hi, target):
    if hi >= lo:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            return binarySearch(arr, lo, mid - 1, target)
          
        return binarySearch(arr, mid + 1, hi, target)
    return -1
  
def expoSearch(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
          
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
      
    return binarySearch( arr, i // 2, min(i, n-1), target)
      
arr = [2, 3, 4, 10, 40]
x = 1
result = expoSearch(arr, x)
if result == -1:
    print ("Element %d not found in the array" %(result))
else:
    print ("Element %d is present at index %d" %(x, result))