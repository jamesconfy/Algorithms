def lastStoneWeight(stones=[1, 4, 2, 7, 8, 1]):
    while len(stones) > 1:
        stones.sort(reverse=True)
        if stones[0] == stones[1] and len(stones) == 2:
            return 0
        if stones[0] == stones[1] and len(stones) > 2:
            stones = stones[2:]
        elif stones[0] != stones[1]:
            appendVal = stones[0] - stones[1]
            stones.append(appendVal)
            stones = stones[2:]

    return min(stones) if stones else 0

stones = [2,2]
print(lastStoneWeight(stones))
