def parallelogramdiagonalanalyzer():
    print("Parallelogram Diagonal Analyzer :")

    diagonal1 = float(input("Enter length of diagonal 1: "))
    diagonal2 = float(input("Enter length of diagonal 2: "))

    midpoint1 = float(input("Enter first half of diagonal 1: "))
    midpoint2 = float(input("Enter second half of diagonal 1: "))
    midpoint3 = float(input("Enter first half of diagonal 2: "))
    midpoint4 = float(input("Enter second half of diagonal 2: "))

    if diagonal1 > 0 and diagonal2 > 0:
        print("Diagonal 1 =", diagonal1)
        print("Diagonal 2 =", diagonal2)

        if midpoint1 == midpoint2 and midpoint3 == midpoint4:
            print("Both diagonals bisect each other.")
            print("The diagonal property of a parallelogram is satisfied.")
        else:
            print("The diagonals do not bisect each other equally.")

        if diagonal1 == diagonal2:
            print("The diagonals are equal.")
        else:
            print("The diagonals are not equal.")
    else:
        print("Diagonal lengths must be greater than zero.")

parallelogramdiagonalanalyzer()