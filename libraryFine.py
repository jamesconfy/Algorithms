# dateCalendar = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }

def libraryFine(d1=5, m1=10, y1=2018, d2=5, m2=10, y2=2018):
    if m1 == m2 and y1 == y2 and d1-d2 > 0:
        return (d1 - d2) * 15

    elif y1 == y2 and m1 > m2:
       return (m1 - m2) * 500

    elif y1 > y2:
        return (y1 - y2) * 10000

    return 0

print(libraryFine(d1=6, m1=6, y1=2015, d2=9, m2=6, y2=2016))
