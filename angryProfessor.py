def angryprofessor(students, k):
    count = 0
    for student in students:
        if student <= 0:
            count += 1

    if count >= k:
        return "YES"
    return "NO"

