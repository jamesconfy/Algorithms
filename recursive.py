def printFun(test):
    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(test, end=" ")
        return


print(printFun(3))