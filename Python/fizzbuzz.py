def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0 and i % 5 != 0:
        return "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        return "Buzz"
    else:
        return i


if __name__ == "__main__": #pragma: no cover
    for i in range(1, 100**50):
        print(fizzbuzz(i))