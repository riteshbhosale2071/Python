def find():
    t = ((1, 2, 3),
     (4, 5, 6),
     (7, 8, 9))

    diagonal_sum = 0

    for i in range(len(t)):
        diagonal_sum += t[i][i]

    print("Diagonal Sum:", diagonal_sum)

find()