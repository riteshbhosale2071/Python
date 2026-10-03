def volumedifferencecalc():
    print("Volume Difference Calculator :")

    print("\nEnter dimensions of Shape 1:")
    length1 = float(input("Enter length: "))
    width1 = float(input("Enter width: "))
    height1 = float(input("Enter height: "))

    print("\nEnter dimensions of Shape 2:")
    length2 = float(input("Enter length: "))
    width2 = float(input("Enter width: "))
    height2 = float(input("Enter height: "))

    if length1 <= 0 or width1 <= 0 or height1 <= 0:
        print("Shape 1 dimensions must be greater than zero.")
        return

    if length2 <= 0 or width2 <= 0 or height2 <= 0:
        print("Shape 2 dimensions must be greater than zero.")
        return

    volume1 = length1 * width1 * height1
    volume2 = length2 * width2 * height2

    difference = abs(volume1 - volume2)

    print("\nResults :")
    print("Volume of Shape 1:", round(volume1, 2))
    print("Volume of Shape 2:", round(volume2, 2))
    print("Volume Difference:", round(difference, 2))

    if volume1 > volume2:
        print("Shape 1 has the greater volume.")
    elif volume2 > volume1:
        print("Shape 2 has the greater volume.")
    else:
        print("Both shapes have equal volume.")

volumedifferencecalc()