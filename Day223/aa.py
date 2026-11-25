def parallellineschecker():
    print("Parallel Lines Checker")
    print("1. Check Using Slopes")
    print("2. Check Using Line Equations")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("Enter coordinates of first line:")
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        print("Enter coordinates of second line:")
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))
        x4 = float(input("Enter x4: "))
        y4 = float(input("Enter y4: "))

        if x1 == x2 and x3 == x4:
            if x1 == x3:
                print("Both lines are coincident, not distinct parallel lines.")
            else:
                print("The lines are parallel.")
            return

        if x1 == x2 or x3 == x4:
            print("The lines are not parallel.")
            return

        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        if abs(slope1 - slope2) < 1e-9:
            print("The lines have equal slopes.")
            if abs((y1 - slope1 * x1) - (y3 - slope2 * x3)) < 1e-9:
                print("The lines are coincident.")
            else:
                print("The lines are parallel.")
        else:
            print("The lines are not parallel.")

    elif choice == "2":
        print("Enter coefficients of first line (A1x + B1y + C1 = 0):")
        a1 = float(input("Enter A1: "))
        b1 = float(input("Enter B1: "))
        c1 = float(input("Enter C1: "))

        print("Enter coefficients of second line (A2x + B2y + C2 = 0):")
        a2 = float(input("Enter A2: "))
        b2 = float(input("Enter B2: "))
        c2 = float(input("Enter C2: "))

        if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
            print("Invalid line equation.")
            return

        if abs(a1 * b2 - a2 * b1) < 1e-9:
            if abs(a1 * c2 - a2 * c1) < 1e-9 and abs(b1 * c2 - b2 * c1) < 1e-9:
                print("The lines are coincident.")
            else:
                print("The lines are parallel.")
        else:
            print("The lines are not parallel.")

    else:
        print("Invalid choice.")

parallellineschecker()