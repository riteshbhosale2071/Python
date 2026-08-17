def ratiocomparison():
    a = float(input("Enter first value of Ratio 1: "))
    b = float(input("Enter second value of Ratio 1: "))

    c = float(input("Enter first value of Ratio 2: "))
    d = float(input("Enter second value of Ratio 2: "))

    if b == 0 or d == 0:
        print("The second value of a ratio cannot be zero.")
        return

    ratio1 = a / b
    ratio2 = c / d

    print("Ratio 1:", a, ":", b)
    print("Ratio 2:", c, ":", d)

    if ratio1 > ratio2:
        print("Ratio 1 is greater.")
    elif ratio1 < ratio2:
        print("Ratio 2 is greater.")
    else:
        print("Both ratios are equal.")

ratiocomparison()