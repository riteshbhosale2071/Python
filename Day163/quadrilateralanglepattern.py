def quadrilateralanglepattern():
    print("Quadrilateral Angle Pattern Generator :")

    print("Choose an angle pattern:")
    print("1. Four equal angles")
    print("2. Two pairs of equal angles")
    print("3. One right angle and three unknown angles")
    print("4. Custom angle pattern")

    choice = input("Enter your choice: ")

    if choice == "1":
        angle = 360 / 4

        print("Angle 1:", angle, "degrees")
        print("Angle 2:", angle, "degrees")
        print("Angle 3:", angle, "degrees")
        print("Angle 4:", angle, "degrees")
        print("Pattern: Four equal angles")

    elif choice == "2":
        angle1 = float(input("Enter the first angle: "))
        angle2 = float(input("Enter the second angle: "))

        angle3 = angle1
        angle4 = angle2

        total = angle1 + angle2 + angle3 + angle4

        if total == 360:
            print("Angle 1:", angle1, "degrees")
            print("Angle 2:", angle2, "degrees")
            print("Angle 3:", angle3, "degrees")
            print("Angle 4:", angle4, "degrees")
            print("Pattern: Two pairs of equal angles")
        else:
            print("Invalid pattern.")
            print("The sum of the angles must be 360 degrees.")

    elif choice == "3":
        angle1 = 90
        remaining = 360 - angle1

        angle2 = float(input("Enter angle 2: "))
        angle3 = float(input("Enter angle 3: "))
        angle4 = remaining - angle2 - angle3

        if angle2 > 0 and angle3 > 0 and angle4 > 0:
            print("Angle 1:", angle1, "degrees")
            print("Angle 2:", angle2, "degrees")
            print("Angle 3:", angle3, "degrees")
            print("Angle 4:", angle4, "degrees")
        else:
            print("Invalid angle values.")

    elif choice == "4":
        angle1 = float(input("Enter angle 1: "))
        angle2 = float(input("Enter angle 2: "))
        angle3 = float(input("Enter angle 3: "))
        angle4 = float(input("Enter angle 4: "))

        total = angle1 + angle2 + angle3 + angle4

        if total == 360:
            print("The angle pattern is valid.")
            print("Total angle:", total, "degrees")
        else:
            print("The angle pattern is invalid.")
            print("The total must be 360 degrees.")

    else:
        print("Invalid choice.")

quadrilateralanglepattern()