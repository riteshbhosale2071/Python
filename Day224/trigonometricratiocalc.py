import math

def trigonometricratiocalc():
    print("Trigonometric Ratio Calculator")
    print("1. Find sin, cos and tan")
    print("2. Find cosec, sec and cot")
    print("3. Find All Six Trigonometric Ratios")
    print("4. Find Angle Using a Ratio")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        print("sin =", round(math.sin(radian), 4))
        print("cos =", round(math.cos(radian), 4))

        if math.isclose(math.cos(radian), 0, abs_tol=1e-10):
            print("tan = Undefined")
        else:
            print("tan =", round(math.tan(radian), 4))

    elif choice == "2":
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        sine = math.sin(radian)
        cosine = math.cos(radian)

        if math.isclose(sine, 0, abs_tol=1e-10):
            print("cosec = Undefined")
        else:
            print("cosec =", round(1 / sine, 4))

        if math.isclose(cosine, 0, abs_tol=1e-10):
            print("sec = Undefined")
        else:
            print("sec =", round(1 / cosine, 4))

        if math.isclose(sine, 0, abs_tol=1e-10):
            print("cot = Undefined")
        else:
            print("cot =", round(cosine / sine, 4))

    elif choice == "3":
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        sine = math.sin(radian)
        cosine = math.cos(radian)

        print("sin =", round(sine, 4))
        print("cos =", round(cosine, 4))
        print("tan =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else round(sine / cosine, 4))
        print("cosec =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else round(1 / sine, 4))
        print("sec =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else round(1 / cosine, 4))
        print("cot =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else round(cosine / sine, 4))

    elif choice == "4":
        ratio = float(input("Enter trigonometric ratio value: "))

        if not -1 <= ratio <= 1:
            print("Ratio must be between -1 and 1.")
            return

        angle = math.degrees(math.asin(ratio))
        print("Principal Angle =", round(angle, 2), "degrees")

    else:
        print("Invalid choice.")

trigonometricratiocalc()