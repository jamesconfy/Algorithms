def beautifyDays(i, j, k):
    count = 0
    for z in range(i, j+1):
        day = str(z)
        newday = int(day)
        reday = int(day[::-1])
        if (newday - reday) % k == 0:
            count += 1

    return count

i = 20
j = 23
k = 6
print(beautifyDays(i , j, k))