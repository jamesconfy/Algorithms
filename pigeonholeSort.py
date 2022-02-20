def pigeonholeSort(arr):
    min = arr[0]
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]

        if arr[i] > max:
            max = arr[i]

    size = max - min + 1
    ph = [0 for i in range(size)]

    for x in arr:
        assert type(x) is int, "integers only please"
        ph[x - min] += 1

    i = 0
    for count in range(size):
        while ph[count] > 0:
            ph[count] -= 1
            arr[i] = count + min
            i += 1

    print(arr)




arr = [2, -10, 10, 20, 40, 30, 15, -10, -10]
pigeonholeSort(arr)