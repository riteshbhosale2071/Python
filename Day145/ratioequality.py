def ratioequality():
    print("Enter the first ratio:")
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))

    print("\nEnter the second ratio:")
    c = float(input("Enter first value: "))
    d = float(input("Enter second value: "))

    if b == 0 or d == 0:
        print("Denominator cannot be zero.")
        return

    ratio1 = a / b
    ratio2 = c / d

    print("\nFirst Ratio:", ratio1)
    print("Second Ratio:", ratio2)

    if ratio1 == ratio2:
        print("The ratios are Equal.")
    else:
        print("The ratios are Not Equal.")

ratioequality()