def trapeziumsiderecovery():
    print("Trapezium Side Recovery :")

    print("1. Find missing non-parallel side")
    print("2. Find missing parallel side")
    print("3. Find both non-parallel sides in an isosceles trapezium")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        area = float(input("Enter trapezium area: "))
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))
        height = float(input("Enter height: "))

        if area <= 0 or a < 0 or b < 0 or height <= 0:
            print("Enter valid values.")
            return

        calculated_area = 0.5 * (a + b) * height

        if abs(calculated_area - area) > 0.01:
            print("The given dimensions are inconsistent.")
            return

        horizontal_offset = float(input("Enter horizontal offset of the missing side: "))

        side = (height ** 2 + horizontal_offset ** 2) ** 0.5
        print("Missing Non-Parallel Side:", round(side, 2))

    elif choice == 2:
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

    elif choice == 3:
        height = float(input("Enter trapezium height: "))
        longer_base = float(input("Enter longer parallel side: "))
        shorter_base = float(input("Enter shorter parallel side: "))

        if height <= 0 or longer_base <= shorter_base or shorter_base < 0:
            print("Enter valid dimensions.")
            return

        offset = (longer_base - shorter_base) / 2
        side = (height ** 2 + offset ** 2) ** 0.5

        print("First Non-Parallel Side:", round(side, 2))
        print("Second Non-Parallel Side:", round(side, 2))

    else:
        print("Invalid choice.")

trapeziumsiderecovery()