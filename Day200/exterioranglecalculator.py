def exterioranglecalculator():
    print("Exterior Angle Calculator")
    print("1. Calculate exterior angle of a polygon")
    print("2. Calculate exterior angle of a regular polygon")
    print("3. Calculate exterior angle using interior angle")

    choice = input("Enter your choice: ")

    if choice == "1":
        sides = int(input("Enter the number of sides: "))

        if sides >= 3:
            angle = 360 / sides
            print("Exterior angle of a regular polygon:", angle, "degrees")
        else:
            print("A polygon must have at least 3 sides.")

    elif choice == "2":
        sides = int(input("Enter the number of sides: "))

        if sides >= 3:
            angle = 360 / sides
            print("Each exterior angle:", angle, "degrees")
        else:
            print("Invalid number of sides.")

    elif choice == "3":
        interior = float(input("Enter the interior angle in degrees: "))

        if 0 < interior < 180:
            exterior = 180 - interior
            print("Exterior angle:", exterior, "degrees")
        else:
            print("Invalid interior angle.")

    else:
        print("Invalid choice.")

exterioranglecalculator()