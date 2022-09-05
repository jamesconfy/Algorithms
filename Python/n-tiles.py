def recur_tiles(arr, new_arr=[]):
    n = len(arr)
    n1 = len(new_arr)
    for i in range(n1):
        for j in range(n):
            if i == j:
                new_tiles = arr[i]
            else:
                new_tiles = new_arr[i] + arr[j]
            new_arr.append(new_tiles)

    new_arr = list(set(new_arr))
    count = len(new_arr)
    return arr, sorted(new_arr), count

    # for i in range(len(new_arr)):
    #     for j in range(len(arr)):
    #         if i == j:
    #             new_tiles = new_arr[i]
    #         else:
    #             new_tiles = new_arr[i] + arr[j]
    #         new_arr.append(new_tiles)

    # return arr, new_arr

def n_tiles(arr, new_arr=[]):
    if new_arr == []:
        new_arr = arr

    i = 0
    new_arr = [''] * len(arr)
    while i < len(arr):
        arr, new_arr, count = recur_tiles(arr, new_arr)

        i += 1

    # count = len(set(new_arr)) - 2
    return arr, sorted(set(new_arr)), count

arr = "AAB"
print(n_tiles(arr))