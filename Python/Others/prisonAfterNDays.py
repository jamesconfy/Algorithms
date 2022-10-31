def prisonAfterNDays(cells, n):
    n = n % 14 if n % 14 != 0 else 14
    for _ in range(n):
        newCells = [0]*len(cells)
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                newCells[i] = 1

        cells = newCells
    return cells

l = [1, 0,0,1,0,0,1,0]
n = 10000000000000000

print(prisonAfterNDays(l, n))
