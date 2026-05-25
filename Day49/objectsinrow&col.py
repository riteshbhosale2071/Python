def count():
    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    for i in matrix:
        print("Row Count =", sum(i))

    for j in range(len(matrix[0])):

        count = 0

        for i in range(len(matrix)):
            count += matrix[i][j]

        print("Column Count =", count)

count()