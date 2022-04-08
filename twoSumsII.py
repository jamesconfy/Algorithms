def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i != j:
#        print(i, j)
        val = numbers[i] + numbers[j]
        if val == target:
            return [i+1, j+1]
        elif val > target:
            j -= 1
        else:
            i += 1

    # for i in range(len(nums)):
    #     s = target - nums[i]
    #     if s in nums and nums.index(s) != i:
    #         return (i+1, nums.index(s)+1)


print(twoSum([2, 3, 4, 6, 9, 11], 10))
