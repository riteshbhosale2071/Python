def missinganglecalculator():
    print("Missing Angle Calculator")
    print("1. Find the third angle of a triangle")
    print("2. Find a missing angle in a straight line")

    choice = input("Enter your choice (1 or 2): ")

    try:
        if choice == "1":
            angle1 = float(input("Enter first angle: "))
            angle2 = float(input("Enter second angle: "))

            if angle1 <= 0 or angle2 <= 0:
                print("Angles must be greater than zero.")
                return

            if angle1 + angle2 >= 180:
                print("The sum of the given angles must be less than 180.")
                return

            missing_angle = 180 - (angle1 + angle2)
            print("Missing angle:", round(missing_angle, 2), "degrees")

        elif choice == "2":
            angle = float(input("Enter the known angle: "))

            if angle <= 0 or angle >= 180:
                print("Angle must be between 0 and 180 degrees.")
                return

            missing_angle = 180 - angle
            print("Missing angle:", round(missing_angle, 2), "degrees")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Please enter valid numeric values.")

missinganglecalculator()