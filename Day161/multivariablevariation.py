def multivariablevariation():
    print("Multi-Variable Variation Calculator :")
    print("Formula: z = kxy")

    k = float(input("Enter variation constant k: "))
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))

    z = k * x * y

    print("Value of z =", z)

multivariablevariation()