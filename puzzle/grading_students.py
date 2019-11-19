def gradingStudents(grades):
    op = []
    for g in grades:
        if g >= 38:
            div_five = g // 5
            if ((div_five + 1) * 5) - g < 3:
                op.append((div_five + 1) * 5)
            else:
                op.append(g)
        else:
            op.append(g)
    return op

grades = [73, 67, 40, 33]
print(gradingStudents(grades))