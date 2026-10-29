def correspondinganglecalculator():
    print("Corresponding Angle Calculator")
    print("1. Find the corresponding angle")
    print("2. Check corresponding angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle = float(input("Enter the given angle in degrees: "))

        if 0 <= angle <= 180:
            print("Corresponding angle:", angle, "degrees")
        else:
            print("Invalid angle.")

    elif choice == "2":
        angle1 = float(input("Enter the first angle in degrees: "))
        angle2 = float(input("Enter the second angle in degrees: "))

        if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
            if abs(angle1 - angle2) < 0.000001:
                print("The angles are equal and may be corresponding angles.")
            else:
                print("The angles are not equal, so they are not corresponding angles.")
        else:
            print("Invalid angles.")

    else:
        print("Invalid choice.")

correspondinganglecalculator()