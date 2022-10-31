def findJudge(n, trust):
    n = len(trust)
    if n == 1:
            return 1

    s=set()
    mydict = dict()
    for l in trust:
        s.add(l[0])
        if l[1] in mydict:
            mydict[l[1]] += 1
        else:
            mydict[l[1]] = 1
        
    for i, j in mydict.items():
        if j == n and i not in s:
            return i
        
    return -1

print(findJudge(5, [[2,3], [1,3], [4, 3]]))