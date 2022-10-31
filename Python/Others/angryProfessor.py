def angryprofessor(students, k):
    count = 0
    for student in students:
        if student <= 0:
            count += 1

    if count >= k:
        return "YES"
    return "NO"

students = [1, -3, 4, 5,-6 ,4,-5,-6,4]
k = 4
print(angryprofessor(students, k))