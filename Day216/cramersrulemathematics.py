def cramersrulemathematics():
    print("Cramer's Rule Mathematics Toolkit")

    n = int(input("Enter the number of variables (2 or 3): "))

    if n not in [2, 3]:
        print("Please enter 2 or 3 variables.")
        return

    coefficients = []
    constants = []

    for i in range(n):
        row = []

        print(f"\nEquation {i + 1}:")
        for j in range(n):
            value = float(input(f"Enter coefficient of variable {j + 1}: "))
            row.append(value)

        constant = float(input("Enter constant value: "))
        coefficients.append(row)
        constants.append(constant)

    if n == 2:
        a, b = coefficients[0]
        c, d = coefficients[1]

        determinant = a * d - b * c

        if determinant == 0:
            print("\nCramer's Rule cannot find a unique solution.")
            return

        dx = constants[0] * d - b * constants[1]
        dy = a * constants[1] - constants[0] * c

        x = dx / determinant
        y = dy / determinant

        print("\nDeterminant D:", determinant)
        print("Determinant Dx:", dx)
        print("Determinant Dy:", dy)
        print("\nSolution:")
        print("x =", round(x, 2))
        print("y =", round(y, 2))

    else:
        a, b, c = coefficients[0]
        d, e, f = coefficients[1]
        g, h, i = coefficients[2]

        determinant = (
            a * (e * i - f * h)
            - b * (d * i - f * g)
            + c * (d * h - e * g)
        )

        if determinant == 0:
            print("\nCramer's Rule cannot find a unique solution.")
            return

        dx = (
            constants[0] * (e * i - f * h)
            - b * (constants[1] * i - f * constants[2])
            + c * (constants[1] * h - e * constants[2])
        )

        dy = (
            a * (constants[1] * i - f * constants[2])
            - constants[0] * (d * i - f * g)
            + c * (d * constants[2] - constants[1] * g)
        )

        dz = (
            a * (e * constants[2] - constants[1] * h)
            - b * (d * constants[2] - constants[1] * g)
            + constants[0] * (d * h - e * g)
        )

        x = dx / determinant
        y = dy / determinant
        z = dz / determinant

        print("\nDeterminant D:", determinant)
        print("Determinant Dx:", dx)
        print("Determinant Dy:", dy)
        print("Determinant Dz:", dz)

        print("\nSolution:")
        print("x =", round(x, 2))
        print("y =", round(y, 2))
        print("z =", round(z, 2))

cramersrulemathematics()