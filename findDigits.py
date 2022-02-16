def findDigits(d):
    fd = [x for x in str(d)]
    count = 0
    for val in fd:
        val = int(val)
        if d % val == 0:
            count += 1

    return count

print(findDigits(125))
