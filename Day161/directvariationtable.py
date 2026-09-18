def directvariationtable():
    print("Direct Variation Table Generator :")

    k = float(input("Enter variation constant k: "))
    n = int(input("Enter number of x values: "))

    print("Direct Variation: y = kx")
    print("x\t\ty")

    for i in range(n):
        x = float(input("Enter x value: "))
        y = k * x
        print(x, "\t\t", y)

directvariationtable()