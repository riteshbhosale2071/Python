def perpendicularline():
    print("Perpendicular Line Detector")
    print("1. Check using slopes")
    print("2. Check using line equations")

    choice = input("Enter your choice: ")

    if choice == "1":
        m1 = float(input("Enter slope of first line: "))
        m2 = float(input("Enter slope of second line: "))

        if abs(m1 * m2 + 1) < 0.000001:
            print("The lines are perpendicular.")
        elif m1 == 0 and m2 == 0:
            print("The lines are parallel, not perpendicular.")
        else:
            print("The lines are not perpendicular.")

    elif choice == "2":
        print("Enter line equations in the form ax + by + c = 0")

        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))

        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        if abs(a1 * a2 + b1 * b2) < 0.000001:
            print("The lines are perpendicular.")
        else:
            print("The lines are not perpendicular.")

    else:
        print("Invalid choice.")

perpendicularline()