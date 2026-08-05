def diagonalcomparison():
    diagonal1 = float(input("Enter the length of the first diagonal: "))
    diagonal2 = float(input("Enter the length of the second diagonal: "))

    if diagonal1 > diagonal2:
        print("First diagonal is longer.")
        print("Difference:", diagonal1 - diagonal2)
    elif diagonal2 > diagonal1:
        print("Second diagonal is longer.")
        print("Difference:", diagonal2 - diagonal1)
    else:
        print("Both diagonals are equal.")

diagonalcomparison()