def square():
    print("Enter the elements of the 3 × 3 matrix:")

    matrix = []

    for i in range(3):
        row = []
        for j in range(3):
            num = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(num)
        matrix.append(row)

    magic_sum = sum(matrix[0])

    is_magic = True

    for row in matrix:
        if sum(row) != magic_sum:
            is_magic = False

    for j in range(3):
        column_sum = 0
        for i in range(3):
            column_sum += matrix[i][j]
        if column_sum != magic_sum:
            is_magic = False

    diagonal1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    diagonal2 = matrix[0][2] + matrix[1][1] + matrix[2][0]

    if diagonal1 != magic_sum or diagonal2 != magic_sum:
        is_magic = False

    print("\nMatrix:")
    for row in matrix:
        print(row)

    if is_magic:
        print("\nIt is a Magic Square.")
    else:
        print("\nIt is NOT a Magic Square.")

square()