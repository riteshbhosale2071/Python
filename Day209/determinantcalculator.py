def determinantcalculator():
    try:
        print("Enter the elements of a 2×2 matrix:")

        a = float(input("Enter a11: "))
        b = float(input("Enter a12: "))
        c = float(input("Enter a21: "))
        d = float(input("Enter a22: "))

        determinant = (a * d) - (b * c)

        print("\nMatrix:")
        print(f"| {a}  {b} |")
        print(f"| {c}  {d} |")

        print("\nDeterminant:", round(determinant, 4))

        if determinant == 0:
            print("The matrix is singular.")
        else:
            print("The matrix is non-singular.")

    except ValueError:
        print("Please enter valid numeric values.")

determinantcalculator()