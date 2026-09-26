def equationtypeclassifier():
    print("Equation Type Classifier :")

    number_of_equations = int(input("Enter the number of equations: "))

    if number_of_equations <= 0:
        print("Number of equations must be greater than zero.")
        return

    for i in range(number_of_equations):
        print("\nEquation", i + 1, ":")

        print("Enter coefficients for ax^2 + bx + c = 0")

        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter constant c: "))

        print("\nEquation:", a, "x^2 +", b, "x +", c, "= 0")

        if a == 0 and b == 0:
            if c == 0:
                print("Equation Type: Identity equation")
                print("Solutions: Infinitely many")
            else:
                print("Equation Type: Contradictory equation")
                print("Solutions: No solution")

        elif a == 0:
            print("Equation Type: Linear equation")

            solution = -c / b
            print("Solution: x =", round(solution, 2))

        else:
            print("Equation Type: Quadratic equation")

            discriminant = b * b - 4 * a * c

            print("Discriminant:", round(discriminant, 2))

            if discriminant > 0:
                print("Root Type: Two distinct real roots")

                root1 = (-b + discriminant ** 0.5) / (2 * a)
                root2 = (-b - discriminant ** 0.5) / (2 * a)

                print("Root 1:", round(root1, 2))
                print("Root 2:", round(root2, 2))

            elif discriminant == 0:
                print("Root Type: Two equal real roots")

                root = -b / (2 * a)

                print("Root:", round(root, 2))

            else:
                print("Root Type: Complex roots")
                print("The equation has no real roots.")

    print("\nEquation Classification Completed.")

equationtypeclassifier()