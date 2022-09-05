def swapBits(val, P1, P2, N):
    result = ""
    while val > 0:
        result += str(val % 2)
        val = int(val / 2)


    result = list(result[len(result)::-1])
    totalL = P2 + N
    while len(result) < totalL:
        result.insert(0, "0")

    result.reverse()
    result[P1:P1+N], result[P2:P2+N] = result[P2:P2+N], result[P1:P1+N]

    result.reverse()
    return int("".join(result), 2)


    


print(swapBits(47, 1, 5, 3))
#print(int("101111", 2))