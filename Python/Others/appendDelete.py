def appendDelete(s, t, k):
    # if len(s) > len(t):
    #     v = len(s) - len(t)
    #     for i in range(v):
    #         t += str(i)

    # if len(s) < len(t):
    #     v = len(t) - len(s)
    #     for i in range(v):
    #         s += str(i)

    # return s, t

    i, l = ([a == b for a, b in zip(s, t)] + [False]).index(False) * 2, len(s+t)
    return 'Yes' if k >= l or k >= l - i and ~(k - l + i) & 1 else 'No'

s = 'aba'
t = 'aba'
k = 7
print(appendDelete(s, t, k))