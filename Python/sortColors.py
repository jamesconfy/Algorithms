def sortColors(color):
    for i in range(len(color)-1):
        for j in range(i+1, len(color)):
            if color[i] > color[j]:
                color[i], color[j] = color[j], color[i]

    return color

color = [1, 0, 2, 3, 4, 0, 1, 2, 3]
print(sortColors(color))