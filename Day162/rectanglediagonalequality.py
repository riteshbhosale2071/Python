def rectanglediagonalequality():
    print("Rectangle Diagonal Equality Checker :")

    diagonal1 = float(input("Enter length of diagonal 1: "))
    diagonal2 = float(input("Enter length of diagonal 2: "))

    if diagonal1 == diagonal2:
        print("The diagonals are equal.")
        print("The rectangle diagonal property is satisfied.")
    else:
        print("The diagonals are not equal.")
        print("The rectangle diagonal property is not satisfied.")

rectanglediagonalequality()