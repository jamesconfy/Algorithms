def twoSum(nums, target):
    for i in range(len(nums)):
        s = target -nums[i]
        if s in nums and nums.index(s) != i:
            return (i, nums.index(s))
        

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))