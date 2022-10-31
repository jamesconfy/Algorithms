def simpleTextEditor(S, queries):
    prev = []
    prev_value = []
    for q in queries:
        if int(q[0]) == 1:
            S += q[2:]
            prev.append(1)
            prev_value.append(len(S) - len(q[2:]))

        elif int(q[0]) == 2:
            k = len(S) - int(q[2:])
            prev.append(2)
            prev_value.append(S[k:])
            S = S[:k]

        elif int(q[0]) == 3:
            k = int(q[2:])
            print(S[k-1])
            #prev = None
#            prev_value = None

        elif int(q[0]) == 4:
            if prev:
                curr = prev.pop()
                curr_value = prev_value.pop()
                if curr == 1:
                    S = S[:curr_value]
                elif curr == 2:
                    S += curr_value

        else:
            continue


    #print(prev, prev_value)
    #print(S)



S=''
#queries=['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']
queries=['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1']
simpleTextEditor(S, queries)