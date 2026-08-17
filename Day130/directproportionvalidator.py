def directproportionvalidator():
    x1 = float(input("Enter first X value: "))
    y1 = float(input("Enter first Y value: "))
    x2 = float(input("Enter second X value: "))
    y2 = float(input("Enter second Y value: "))

    if x1 == 0 or x2 == 0:
        print("X values cannot be zero.")
        return

    ratio1 = y1 / x1
    ratio2 = y2 / x2

    print("First Ratio (Y/X):", ratio1)
    print("Second Ratio (Y/X):", ratio2)

    if ratio1 == ratio2:
        print("The values are in Direct Proportion.")
    else:
        print("The values are not in Direct Proportion.")

directproportionvalidator()