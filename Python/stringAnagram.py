def stringAnagram(dictionary, query):
    answer = []
    dict = {}

    for i in range(len(dictionary)):
        di = "".join(sorted(list(dictionary[i])))
        if di in dict:
            dict[di] += 1
        else:
            dict[di] = 1
        
    for q in query:
        q = "".join(sorted(list(q)))
        if q in dict:
            answer.append(dict.get(q))
        else:
            answer.append(0)
        
    return answer

dictionary = ['hack', 'arc', 'hacker', 'rank', 'rs', 'kanr']
query = ['qs', 'bs', 'ackh', 'ankr']
print(stringAnagram(dictionary, query))