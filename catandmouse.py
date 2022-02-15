def catMouse(cat1, cat2, mouse):
    if abs(cat1 - mouse) == abs(cat2 - mouse):
        return "Mouse C"
    elif abs(cat1 - mouse) < abs(cat2 - mouse):
        return "Cat A"
    else:
        return "Cat B"

print(catMouse(1, 2, 3))