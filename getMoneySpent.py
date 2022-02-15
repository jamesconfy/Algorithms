def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    maxValue = -1
    for val in keyboards:
        for val2 in drives:
            value = val + val2
            if value > maxValue and value <= b:
                maxValue = value
              

    return maxValue

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]
print(getMoneySpent(keyboards=keyboards, drives=drives, b=b))