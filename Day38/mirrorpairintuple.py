def find():
    t = ((1, 2, 3),
     (4, 5, 6))

    transpose = []

    for i in range(len(t[0])):
        row = []

        for j in range(len(t)):
            row.append(t[j][i])

        transpose.append(tuple(row))

    print(tuple(transpose))

find()