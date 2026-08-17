def inverseproportion():
    x1 = float(input("Enter first X value: "))
    y1 = float(input("Enter corresponding Y value: "))
    x2 = float(input("Enter second X value: "))

    if x1 == 0 or x2 == 0:
        print("X values cannot be zero.")
        return

    constant = x1 * y1
    y2 = constant / x2

    print("Constant of Proportion:", constant)
    print("Corresponding Y value:", y2)

inverseproportion()