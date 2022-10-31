def numRollsToTarget(n: int, k: int, target: int) -> int:
    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    dp[0][0] = 1

    #print(dp)
    for i in range(1, n+1):
        for j in range(1, target+1):
            dp[i][j] = sum(dp[i-1][max(0, j-k):j])
            #print(dp)

    return dp[-1][-1]%(10**9+7)

print(numRollsToTarget(3, 3, 9))