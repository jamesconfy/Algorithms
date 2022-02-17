from itertools import permutations

def letterTilePossibilities(tiles="AAB"):
    setA = set()
    for i in range(1, len(tiles)+1):
        permvalue = permutations(tiles[:i])
        for per in list(permvalue):
            setA.add("".join(per))

    return sorted(list(setA))

 #   for per in setA:
  #      print("".join(per))
#    return list(setA)

print(letterTilePossibilities())