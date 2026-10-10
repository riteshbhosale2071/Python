def trapeziumdimensionrecovery():
    print("Trapezium Dimension Recovery :")

    print("1. Find missing height")
    print("2. Find missing parallel side")
    print("3. Find area")
    print("4. Find missing side using area")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        area = float(input("Enter trapezium area: "))
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))

        if area <= 0 or a < 0 or b < 0 or a + b == 0:
            print("Enter valid values.")
            return

        height = (2 * area) / (a + b)
        print("Missing Height:", round(height, 2))

    elif choice == 2:
        area = float(input("Enter trapezium area: "))
        height = float(input("Enter height: "))
        a = float(input("Enter known parallel side: "))

        if area <= 0 or height <= 0 or a < 0:
            print("Enter valid values.")
            return

        b = (2 * area / height) - a

        if b < 0:
            print("The given dimensions are inconsistent.")
        else:
            print("Missing Parallel Side:", round(b, 2))

    elif choice == 3:
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))
        height = float(input("Enter height: "))

        if a < 0 or b < 0 or a + b <= 0 or height <= 0:
            print("Enter valid values.")
            return

        area = 0.5 * (a + b) * height
        print("Trapezium Area:", round(area, 2))

    elif choice == 4:
        area = float(input("Enter trapezium area: "))
        height = float(input("Enter height: "))
        known_side = float(input("Enter known parallel side: "))

        if area <= 0 or height <= 0 or known_side < 0:
            print("Enter valid values.")
            return

        missing_side = (2 * area / height) - known_side

        if missing_side <= 0:
            print("The given dimensions are inconsistent.")
        else:
            print("Missing Parallel Side:", round(missing_side, 2))

    else:
        print("Invalid choice.")

trapeziumdimensionrecovery()