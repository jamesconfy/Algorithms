def repeatedString(s='abcac', n=10):   
    # countedA = s.count('a') 
    # lenS = len(s)
    # remainS = s[:n % lenS].count('a')
    # return (countedA * n//lenS) + (remainS)
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

s = 'aba'
n = 10
print(repeatedString(s, n))