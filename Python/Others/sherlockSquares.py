import math

def sherlockSquares(a=24, b=49):
    # count = 0
    # for z in range(a,b+1):
    #     root = math.sqrt(z)
    #     if z == int(root) ** 2:
    #         count += 1

    # return count

    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1 
print(sherlockSquares())