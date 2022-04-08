def isBalanced(s):
    stack = []
    count = 0
    for st in s:
#        stack.append(st)
        if st == "}":
            count -= 1
            if stack and stack[-1] == "{":
                stack.pop()
        elif st == "]":
            count -= 1
            if stack and stack[-1] == "[":
                stack.pop()
        elif st == ")":
            count -= 1
            if stack and stack[-1] == "(":
                stack.pop()
        else:
            stack.append(st)
            count += 1

    return "YES" if count == 0 else "NO"

#     def isBalanced(s):
#     if len(s) % 2 != 0:
#         return 'NO'

#     stack = []
#     closing = ['}', ']', ')']
#     pairs = {'}':'{', ']':'[', ')':'('}
  
#     for bracket in s:
#         if bracket in closing:
#             if not stack or stack.pop() != pairs.get(bracket):
#                 return 'NO'
#         else:
#           stack.append(bracket)
      
#     return 'YES' if not stack else 'NO'

# s = "{{[[(())]]}}"
# print(isBalanced(s))

        

s = "{[(])}"
print(isBalanced(s))

        