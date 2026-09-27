def multipleequationsolver():
    print("Multiple Equation Solver :")
    print("Equations must be in the form:")
    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")

    number_of_systems = int(input("Enter the number of equation systems: "))

    if number_of_systems <= 0:
        print("Number of systems must be greater than zero.")
        return

    for system in range(number_of_systems):
        print("\nSystem", system + 1, ":")

        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        print("\nEquation 1:", a1, "x +", b1, "y =", c1)
        print("Equation 2:", a2, "x +", b2, "y =", c2)

        determinant = a1 * b2 - a2 * b1

        if determinant != 0:
            x = (c1 * b2 - c2 * b1) / determinant
            y = (a1 * c2 - a2 * c1) / determinant

            print("\nUnique Solution:")
            print("x =", round(x, 2))
            print("y =", round(y, 2))

        else:
            if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
                print("\nResult: Infinitely many solutions.")
            else:
                print("\nResult: No solution.")

    print("\nMultiple Equation Solving Completed.")

multipleequationsolver()