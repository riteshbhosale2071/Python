def triangleconstructiondatavalidator():
    print("Triangle Construction Data Validator")
    print("1. Validate Three Side Lengths (SSS)")
    print("2. Validate Two Sides and Included Angle (SAS)")
    print("3. Validate Two Angles and One Side (ASA/AAS)")
    print("4. Validate Three Angles (AAA)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))

        if min(a, b, c) <= 0:
            print("Side lengths must be positive.")
        elif a + b > c and a + c > b and b + c > a:
            print("Valid triangle construction data.")
        else:
            print("Invalid data: Triangle inequality is not satisfied.")

    elif choice == "2":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        angle = float(input("Enter included angle in degrees: "))

        if a <= 0 or b <= 0 or not 0 < angle < 180:
            print("Invalid construction data.")
        else:
            print("Valid triangle construction data using SAS.")

    elif choice == "3":
        angle_a = float(input("Enter first angle in degrees: "))
        angle_b = float(input("Enter second angle in degrees: "))
        side = float(input("Enter a known side length: "))

        if side <= 0 or angle_a <= 0 or angle_b <= 0:
            print("Invalid construction data.")
        elif angle_a + angle_b < 180:
            angle_c = 180 - angle_a - angle_b
            if angle_c > 0:
                print("Valid triangle construction data using ASA/AAS.")
                print("Third Angle =", round(angle_c, 2), "degrees")
            else:
                print("Invalid angle measurements.")
        else:
            print("Invalid data: Sum of two angles must be less than 180 degrees.")

    elif choice == "4":
        a = float(input("Enter first angle: "))
        b = float(input("Enter second angle: "))
        c = float(input("Enter third angle: "))

        if min(a, b, c) <= 0:
            print("Angles must be positive.")
        elif abs(a + b + c - 180) < 1e-9:
            print("Angles can form a triangle.")
            print("Note: AAA determines similarity, not a unique triangle size.")
        else:
            print("Invalid data: Angles must add up to 180 degrees.")

    else:
        print("Invalid choice.")

triangleconstructiondatavalidator()