def cutSticks(sticks=[1, 2, 3]):
    result = []
    while sticks:
        result.append(len(sticks))
        minValue = min(sticks)
        for i in range(len(sticks)):
            sticks[i] -= minValue

        sticks = list(filter(lambda x: x!=0, sticks))

        print(sticks)
    return result

#sticks = [1, 2, 3, 4, 3, 3, 2, 1]
sticks = [8, 8, 14, 10, 3, 5, 14, 12]
print(cutSticks(sticks=sticks))