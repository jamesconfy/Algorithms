# def countArray(arr):
#     arr1 = []
#     maxSum = 0
#     for i in range(len(arr)):
#         arr2 = [arr[i]]
#         for j in range(i+1, len(arr)):
#             if arr2[-1] < arr[j]:
#                 arr2.append(arr[j])
#             if len(arr2) == 3:
#                 break

#         if len(arr2) == 3:
#             if sum(arr2) > maxSum:
#                 arr1.append(arr2)
#                 maxSum = sum(arr2)

#     return arr1[-1] if arr1 else -1

def countArray(arr):
    arr1 = []
    maxSum = 0
    for i in range(1, len(arr)-1):
        maxVal = max(arr[i:])
        minVal = max(arr[:i])
        arr2 = []
        arr2.append(minVal)
        arr2.append(arr[i])
        arr2.append(maxVal)
        mySum = sum(arr2)
        if minVal < arr[i] and maxVal > arr[i] and mySum >= maxSum:
            if sum(arr2) >= maxSum:
                arr1.append(arr2)
                maxSum = sum(arr2)

    return arr1[-1] if arr1 else -1


#arr = [98, 6, 7, 8, 1, 2, 3, 9, 10, 11, 0, 89, 15, 97, 101, 200]
#arr = [3, 4, 2, 1]
arr = [6, 7, 8, 1, 2, 3, 9, 10]
print(countArray(arr))
