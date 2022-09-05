def searchRange(nums=[1], target=1):
    arr = []
    for i in range(len(nums)):
        if nums[i] == target:
            arr.append(i)

    return [arr[0], arr[-1]] if arr else [-1, -1]


print(searchRange())