def permute(list, s):
   if list <= 1:
      return s
   else:
      return [ 
         y + x
         for y in permute(1, s)
         for x in permute(list - 1, s)
      ]
print(permute(1, ["a","b","c","d","3"]))
print(permute(3, ["a","b","c"]))