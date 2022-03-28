def decryptPassword(s):
    # Write your code here
    # res = []
    # i = 0
    # while i < len(s)-1:
    #     if s[i].islower() and s[i+1].isupper():
    #         res.append(s[i+1])
    #         res.append(s[i])
    #         res.append("*")
    #         i += 2
            
    #     elif s[i].isnumeric():
    #         res.insert(0, str(s[i])) 
    #         res.append("0")
    #         i += 1
            
    #     else:
    #         res.append(s[i])
    #         i += 1
        
    # res.append(s[-1])
    # return "".join(res)
    # Write your code here
    res = []
    res1 = [x for x in s if x.isnumeric() and x != "0"]
    i = 0
    lenR = len(res1)
    s = s[lenR:]

    print(res1)

    while i < len(s) - 1:
        if s[i].isupper() and s[i+1].islower():
            res.append(s[i+1])
            res.append(s[i])
            i += 2

        elif s[i] == "0":
            val = res1.pop()
            res.append(val)
            i += 1

        else:
            if s[i] != "*":
                res.append(s[i])
            i += 1

    res.append(s[-1])
    print(res)
    return "".join(res)

print(decryptPassword("pTo*Ta*O"))