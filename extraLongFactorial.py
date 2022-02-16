from math import factorial


def extraLongFactorial(n=30):
    if n == 0:
        return
    return n * factorial(n-1)

print(extraLongFactorial())