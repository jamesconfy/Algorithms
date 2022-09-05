def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # n = len(nums) - k - 1
    # nums = nums[n+1:] + nums[:n+1]

    # for i in range(k):
    #     curr = nums.pop()
    #     nums.insert(0, curr)
    while k > 0:
            nums = [nums[-1]] + nums[:len(nums)-1]
            k -= 1
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))
