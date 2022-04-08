def maxProfit(prices):
    # if prices.sort(reverse=True) == prices:
    #     return 0

    res = []
    for i in range(len(prices)-1):
        # arr = []
        # for j in range(i+1, len(prices)):
        #     val = prices[j] - prices[i]
        #     arr.append(val)

        # res.append(max(arr))
        val = max(prices[i:])
        if prices[i] < val:
            res.append(val - prices[i])

    return max(res) if res and max(res) > 0 else 0


prices = [1, 4, 1]
print(maxProfit(prices))
