def rank():
    students = {
        "Ravi": 450,
        "Priya": 480,
        "Amit": 420,
        "Neha": 470
    }

    ranked = sorted(students.items(), key=lambda x: x[1], reverse=True)

    print("Student Rankings:\n")

    rank = 1

    for name, marks in ranked:
        print(rank, "->", name, "-", marks)
        rank += 1

rank()