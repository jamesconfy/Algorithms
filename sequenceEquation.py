from unittest import result


def sequenceEquation(arr=[5, 2, 1, 3, 4]):
    result = []
    for i in range(len(arr)):
        i = i + 1
#        print(i)
        if i in arr:
            iIdx = arr.index(i) + 1
            print(iIdx)
            if iIdx in arr:
                iiIdx = arr.index(iIdx) + 1
        
        result.append(iiIdx)

    return result


arr = [2, 3, 1]
print(sequenceEquation(arr))