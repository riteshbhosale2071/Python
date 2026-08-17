def directproportion():
    x1 = float(input("Enter first value of X: "))
    y1 = float(input("Enter corresponding value of Y: "))
    x2 = float(input("Enter second value of X: "))

    if x1 == 0:
        print("First X value cannot be zero.")
        return

    constant = y1 / x1
    y2 = constant * x2

    print("Constant of Proportion:", constant)
    print("Corresponding Y value:", y2)

directproportion()