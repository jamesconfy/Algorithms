def possibleChanges(usernames):
    # Write your code here
    answer = []
    for user in usernames:
        res = []
        for i in range(len(user)):
            res.append(ord(user[i]))

        ress = sorted(res)
        j = 0
        while j <= len(user)-1:
            if j == len(user)-1:
                answer.append('NO')
            elif ress[j] < res[j]:
                answer.append('YES')
                j = len(user)-1

            j += 1

    return answer


    # answer = []
    # for user in usernames:
    #     count = 0
    #     for i in range(len(user)):
    #         for j in range(i+1, len(user)):
    #             start = ord(user[i])
    #             if start > ord(user[j]):
    #                 count += 1

    #         if count != 0:
    #             break

    #     if count > 0:
    #         answer.append('YES')
    #     else:
    #         answer.append('NO')
                
    # return answer

print(possibleChanges(['foo', 'bcb', 'baz', 'aab']))