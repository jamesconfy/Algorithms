def fourSum(nums, target):
    unique = set()
    nums.sort()
    n = len(nums)

    for i in range(n-3):
        for j in range(i+1, n-2):
            start = j + 1
            end = n - 1
            while start < end:
                if nums[start] + nums[end] == target - nums[i] - nums[j]:
                    if (nums[i], nums[j], nums[start], nums[end]) not in unique:
                        unique.add((nums[i], nums[j], nums[start], nums[end]))

                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < target - nums[i] - nums[j]:
                    start += 1
                else:
                    end -= 1

    return list(unique)


nums = [-1, 2, -1, 0, 6]
target = 4
print(fourSum(nums, target))
