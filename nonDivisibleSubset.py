def nonDivisibleSubset(s=[19,10,12,10,24,25,22], k=4):
    countMod = [0] * k
    for i in range(len(s)):
        countMod[s[i] % k] += 1
    
    ans = 0
    for i in range(1,k):
        if i < k - i:
            ans += max(countMod[i], countMod[k-i])
        
    # If k is even, only one number of value k / 2 may appear (other wise ex. k = 4, 2+2=4)
    if k % 2 == 0 and countMod[k // 2] > 0:
            ans += 1
    
    # Ex. 14, k = 7. Then 14 % 7 == 0. But, 21 % 7 == 0. Yet: 14 + 21 = 35, 35 % 7 == 0.
    return ans if countMod[0] == 0 else ans + 1

print(nonDivisibleSubset())