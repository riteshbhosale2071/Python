def perpendicularlineschecker():
    print("Perpendicular Lines Checker")
    print("1. Check Using Slopes")
    print("2. Check Using Line Equations")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("Enter first line coordinates:")
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        print("Enter second line coordinates:")
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))
        x4 = float(input("Enter x4: "))
        y4 = float(input("Enter y4: "))

        dx1 = x2 - x1
        dy1 = y2 - y1
        dx2 = x4 - x3
        dy2 = y4 - y3

        if (dx1 == 0 and dy1 == 0) or (dx2 == 0 and dy2 == 0):
            print("Invalid line coordinates.")
            return

        if abs(dx1 * dx2 + dy1 * dy2) < 1e-9:
            print("The lines are perpendicular.")
        else:
            print("The lines are not perpendicular.")

    elif choice == "2":
        print("Enter first line coefficients (A1x + B1y + C1 = 0):")
        a1 = float(input("Enter A1: "))
        b1 = float(input("Enter B1: "))
        c1 = float(input("Enter C1: "))

        print("Enter second line coefficients (A2x + B2y + C2 = 0):")
        a2 = float(input("Enter A2: "))
        b2 = float(input("Enter B2: "))
        c2 = float(input("Enter C2: "))

        if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
            print("Invalid line equation.")
            return

        if abs(a1 * a2 + b1 * b2) < 1e-9:
            print("The lines are perpendicular.")
        else:
            print("The lines are not perpendicular.")

    else:
        print("Invalid choice.")

perpendicularlineschecker()