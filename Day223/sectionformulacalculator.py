def sectionformulacalculator():
    print("Section Formula Calculator")
    print("1. Internal Division")
    print("2. External Division")
    print("3. Find Midpoint")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        m = float(input("Enter first ratio (m): "))
        n = float(input("Enter second ratio (n): "))

        if m <= 0 or n <= 0:
            print("Ratio values must be positive.")
            return

        x = (m * x2 + n * x1) / (m + n)
        y = (m * y2 + n * y1) / (m + n)

        print("Internal Division Point =", (round(x, 2), round(y, 2)))

    elif choice == "2":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        m = float(input("Enter first ratio (m): "))
        n = float(input("Enter second ratio (n): "))

        if m <= 0 or n <= 0 or m == n:
            print("Ratio values must be positive and unequal.")
            return

        x = (m * x2 - n * x1) / (m - n)
        y = (m * y2 - n * y1) / (m - n)

        print("External Division Point =", (round(x, 2), round(y, 2)))

    elif choice == "3":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        x = (x1 + x2) / 2
        y = (y1 + y2) / 2

        print("Midpoint =", (round(x, 2), round(y, 2)))

    else:
        print("Invalid choice.")

sectionformulacalculator()