def utopiantree(n):
    result = [1]
    for i in range(1, n+1):
        if i % 2 == 0:
            newR = result[-1] + 1
        else:
            newR = result[-1] * 2

        result.append(newR)

    return result[-1]

n = 5
print(utopiantree(n))