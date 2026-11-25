import math

def collinearitychecker():
    print("Collinearity Checker")
    print("1. Check Three Points in 2D")
    print("2. Check Three Points in 3D")
    print("3. Check Using Slope")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))

        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        if area < 1e-9:
            print("The three points are collinear.")
        else:
            print("The three points are not collinear.")

    elif choice == "2":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))
        z3 = float(input("Enter z3: "))

        ax, ay, az = x2 - x1, y2 - y1, z2 - z1
        bx, by, bz = x3 - x1, y3 - y1, z3 - z1

        cx = ay * bz - az * by
        cy = az * bx - ax * bz
        cz = ax * by - ay * bx

        if math.isclose(cx, 0, abs_tol=1e-9) and math.isclose(cy, 0, abs_tol=1e-9) and math.isclose(cz, 0, abs_tol=1e-9):
            print("The three points are collinear.")
        else:
            print("The three points are not collinear.")

    elif choice == "3":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        x3 = float(input("Enter x3: "))
        y3 = float(input("Enter y3: "))

        if x1 == x2 == x3:
            print("The points are collinear on a vertical line.")
        elif x1 == x2 or x2 == x3 or x1 == x3:
            print("The points are not collinear.")
        else:
            slope1 = (y2 - y1) / (x2 - x1)
            slope2 = (y3 - y2) / (x3 - x2)

            if abs(slope1 - slope2) < 1e-9:
                print("The points are collinear.")
            else:
                print("The points are not collinear.")

    else:
        print("Invalid choice.")

collinearitychecker()