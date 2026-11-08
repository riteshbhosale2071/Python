def parallelandcoincidentline():
    try:
        print("Enter coefficients of first line (a1x + b1y + c1 = 0)")
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        print("\nEnter coefficients of second line (a2x + b2y + c2 = 0)")
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
            print("Invalid line equation.")
            return

        if a1 * b2 == a2 * b1:
            if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
                print("Result: Lines are coincident.")
                print("Both equations represent the same line.")
            else:
                print("Result: Lines are parallel.")
                print("The lines never intersect.")
        else:
            print("Result: Lines are intersecting.")
            print("The lines meet at one point.")

    except ValueError:
        print("Please enter valid numeric coefficients.")

parallelandcoincidentline()