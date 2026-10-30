def trianglecongruencetester():
    print("Triangle Congruence Tester")
    print("1. Check using SSS (Side-Side-Side)")
    print("2. Check using SAS (Side-Angle-Side)")
    print("3. Check using ASA (Angle-Side-Angle)")
    print("4. Check using AAS (Angle-Angle-Side)")

    choice = input("Enter your choice: ")

    if choice == "1":
        a1 = float(input("Enter first triangle side 1: "))
        b1 = float(input("Enter first triangle side 2: "))
        c1 = float(input("Enter first triangle side 3: "))

        a2 = float(input("Enter second triangle side 1: "))
        b2 = float(input("Enter second triangle side 2: "))
        c2 = float(input("Enter second triangle side 3: "))

        sides1 = sorted([a1, b1, c1])
        sides2 = sorted([a2, b2, c2])

        if min(sides1) > 0 and min(sides2) > 0:
            if sides1[0] + sides1[1] > sides1[2] and sides2[0] + sides2[1] > sides2[2]:
                if all(abs(x - y) < 0.000001 for x, y in zip(sides1, sides2)):
                    print("Triangles are congruent by SSS.")
                else:
                    print("Triangles are not congruent.")
            else:
                print("Invalid triangle measurements.")
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        a1 = float(input("Enter first triangle side 1: "))
        angle1 = float(input("Enter included angle of first triangle: "))
        b1 = float(input("Enter first triangle side 2: "))

        a2 = float(input("Enter second triangle side 1: "))
        angle2 = float(input("Enter included angle of second triangle: "))
        b2 = float(input("Enter second triangle side 2: "))

        if a1 > 0 and b1 > 0 and a2 > 0 and b2 > 0 and 0 < angle1 < 180 and 0 < angle2 < 180:
            if abs(a1 - a2) < 0.000001 and abs(b1 - b2) < 0.000001 and abs(angle1 - angle2) < 0.000001:
                print("Triangles are congruent by SAS.")
            else:
                print("Triangles are not congruent.")
        else:
            print("Invalid measurements.")

    elif choice == "3" or choice == "4":
        a1 = float(input("Enter first triangle angle 1: "))
        b1 = float(input("Enter first triangle angle 2: "))
        s1 = float(input("Enter first triangle side: "))

        a2 = float(input("Enter second triangle angle 1: "))
        b2 = float(input("Enter second triangle angle 2: "))
        s2 = float(input("Enter second triangle side: "))

        if 0 < a1 < 180 and 0 < b1 < 180 and 0 < a2 < 180 and 0 < b2 < 180 and s1 > 0 and s2 > 0:
            if abs(a1 - a2) < 0.000001 and abs(b1 - b2) < 0.000001 and abs(s1 - s2) < 0.000001:
                print("Triangles are congruent by ASA/AAS.")
            else:
                print("Triangles are not congruent.")
        else:
            print("Invalid measurements.")

    else:
        print("Invalid choice.")

trianglecongruencetester()