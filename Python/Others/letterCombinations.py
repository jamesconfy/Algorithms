def letterCombinations(digits):
    if digits == "":
        return []
    char = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
        'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    output = ['']
    temp = []
    for d in digits:
        d1 = char.get(d)
        for i in output:
            for j in d1:
                temp.append(i+j)

        output = temp
        temp = []
    return output


digits = '52'
print(letterCombinations(digits))
