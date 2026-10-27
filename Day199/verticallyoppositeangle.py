def verticallyoppositeangle():
    print("Vertically Opposite Angle Finder")
    print("1. Find the vertically opposite angle")
    print("2. Find all four angles")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle = float(input("Enter the given angle in degrees: "))

        if 0 <= angle <= 180:
            print("Vertically opposite angle:", angle, "degrees")
        else:
            print("Invalid angle.")

    elif choice == "2":
        angle = float(input("Enter one angle in degrees: "))

        if 0 <= angle <= 180:
            opposite = angle
            adjacent = 180 - angle

            print("First angle:", angle, "degrees")
            print("Vertically opposite angle:", opposite, "degrees")
            print("Adjacent angle 1:", adjacent, "degrees")
            print("Adjacent angle 2:", adjacent, "degrees")
        else:
            print("Invalid angle.")

    else:
        print("Invalid choice.")

verticallyoppositeangle()