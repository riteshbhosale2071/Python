def inversevariationtable():
    print("Inverse Variation Table Generator :")

    k = float(input("Enter variation constant k: "))
    n = int(input("Enter number of x values: "))

    print("Inverse Variation: y = k / x")
    print("x\t\ty")

    for i in range(n):
        x = float(input("Enter x value: "))

        if x != 0:
            y = k / x
            print(x, "\t\t", y)
        else:
            print("x cannot be zero.")

inversevariationtable()