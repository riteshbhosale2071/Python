def complementaryanglerelationship():
    print("Complementary Angle Relationship Calculator")
    print("1. Find Complementary Angle")
    print("2. Verify Complementary Angles")
    print("3. Find Sum of Two Angles")
    print("4. Calculate Trigonometric Relationships")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        angle = float(input("Enter an angle in degrees: "))

        if not 0 <= angle <= 90:
            print("Angle must be between 0 and 90 degrees.")
            return

        print("Complementary Angle =", round(90 - angle, 2), "degrees")

    elif choice == "2":
        angle1 = float(input("Enter first angle: "))
        angle2 = float(input("Enter second angle: "))

        if not (0 <= angle1 <= 90 and 0 <= angle2 <= 90):
            print("Angles must be between 0 and 90 degrees.")
            return

        if abs(angle1 + angle2 - 90) < 1e-9:
            print("The angles are complementary.")
        else:
            print("The angles are not complementary.")

    elif choice == "3":
        angle1 = float(input("Enter first angle: "))
        angle2 = float(input("Enter second angle: "))

        print("Sum of Angles =", round(angle1 + angle2, 2), "degrees")

        if abs(angle1 + angle2 - 90) < 1e-9:
            print("The angles form a complementary pair.")
        else:
            print("The angles do not form a complementary pair.")

    elif choice == "4":
        import math

        angle = float(input("Enter angle in degrees: "))

        if not 0 <= angle <= 90:
            print("Angle must be between 0 and 90 degrees.")
            return

        complementary = 90 - angle

        print("sin(θ) =", round(math.sin(math.radians(angle)), 4))
        print("cos(90° - θ) =", round(math.cos(math.radians(complementary)), 4))
        print("cos(θ) =", round(math.cos(math.radians(angle)), 4))
        print("sin(90° - θ) =", round(math.sin(math.radians(complementary)), 4))

    else:
        print("Invalid choice.")

complementaryanglerelationship()