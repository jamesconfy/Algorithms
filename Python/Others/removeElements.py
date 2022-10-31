def removeElements(nums, val):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == val:
            nums[i] = "_"
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1

    return len(nums) - nums.count("_")

nums = [1, 2, 3, 4, 0, 2, 2]
val = 2
print(removeElements(nums, val))
