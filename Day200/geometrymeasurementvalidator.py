def geometrymeasurementvalidator():
    print("Geometry Measurement Validator")
    print("1. Validate triangle sides")
    print("2. Validate triangle angles")
    print("3. Validate rectangle measurements")
    print("4. Validate circle radius")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                print("Valid triangle measurements.")
            else:
                print("Invalid triangle measurements.")
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        a = float(input("Enter first angle: "))
        b = float(input("Enter second angle: "))
        c = float(input("Enter third angle: "))

        if a > 0 and b > 0 and c > 0:
            if abs(a + b + c - 180) < 0.000001:
                print("Valid triangle angles.")
            else:
                print("Invalid triangle angles.")
        else:
            print("Angles must be positive.")

    elif choice == "3":
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        if length > 0 and width > 0:
            print("Valid rectangle measurements.")
            print("Area:", length * width)
            print("Perimeter:", 2 * (length + width))
        else:
            print("Length and width must be positive.")

    elif choice == "4":
        radius = float(input("Enter circle radius: "))

        if radius > 0:
            print("Valid circle radius.")
            print("Diameter:", 2 * radius)
            print("Area:", 3.14159 * radius * radius)
            print("Circumference:", 2 * 3.14159 * radius)
        else:
            print("Radius must be positive.")

    else:
        print("Invalid choice.")

geometrymeasurementvalidator()