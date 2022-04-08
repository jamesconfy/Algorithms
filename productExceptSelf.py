import math

def productExceptSelf(nums):
    answer = []
    for i in range(len(nums)):
        newL = nums[:i] + nums[i+1:]
        result = math.prod(newL)
        answer.append(result)

    return answer

print(productExceptSelf([1, 2, 3, 4, 5, 6, 0, 8, 0, 10, 11]))
