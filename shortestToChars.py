def shortestToChars(s, c):
    answer = []
    for i in range(len(s)):
        j = k = i
        #if s[i] == c:
         #   answer.append(0)
            #break

        while k <= len(s)-1:
            if s[k] == c:
                break
            k += 1

        while j >= 0:
            if s[j] == c:
                break
            j -= 1

        if j < 0:
            answer.append(abs(i-k))
        elif k >= len(s):
            answer.append(abs(i-j))
        else:
            answer.append(min(abs(i-j), abs(i-k)))
    return answer

s = "aaba"
c = "b"
print(shortestToChars(s, c))