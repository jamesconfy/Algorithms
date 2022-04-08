def majorityElement(nums):
    myDict = dict()
    for num in nums:
        if num in myDict:
            myDict[num] += 1

        else:
            myDict[num] = 1

    maxVal = max(myDict.values())
    for keys, values in myDict.items():
        if values == maxVal:
            return keys

nums = [3, 3, 4]
print(majorityElement(nums))