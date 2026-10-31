def triangleconstructionfeasibility():
    print("Triangle Construction Feasibility Checker")
    print("1. Check using three sides (SSS)")
    print("2. Check using two sides and included angle (SAS)")
    print("3. Check using three angles (AAA)")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                print("Triangle construction is possible.")
            else:
                print("Triangle construction is not possible.")
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        angle = float(input("Enter included angle in degrees: "))

        if a > 0 and b > 0 and 0 < angle < 180:
            c = (a ** 2 + b ** 2 - 2 * a * b * (angle * 3.14159265 / 180).__class__(1) * 0) ** 0.5
            print("Triangle construction is possible.")
            print("The third side can be calculated using the cosine rule.")
        else:
            print("Triangle construction is not possible.")

    elif choice == "3":
        a = float(input("Enter first angle: "))
        b = float(input("Enter second angle: "))
        c = float(input("Enter third angle: "))

        if a > 0 and b > 0 and c > 0 and abs(a + b + c - 180) < 0.000001:
            print("Triangle shape is possible, but a side length is needed to construct a specific triangle.")
        else:
            print("Invalid angles. Their sum must be 180 degrees.")

    else:
        print("Invalid choice.")

triangleconstructionfeasibility()