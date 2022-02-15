def viralAdvertising(n):
    liked, cumm = [], 0
    firstPerson = 5
    i = 1
    while i <= n:
        like = int(firstPerson / 2)
        
        print(firstPerson, like, cumm)
        liked.append(like)

        cumm += like
        firstPerson = int(firstPerson / 2) * 3

        i += 1

    return cumm


print(viralAdvertising(5))