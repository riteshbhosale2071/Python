def linesegmentratiodivider():
    print("Line Segment Ratio Divider")
    print("1. Divide a Line Segment in a Given Ratio")
    print("2. Find Ratio of Two Segments")
    print("3. Find Division Point on a Coordinate Plane")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        length = float(input("Enter total line segment length: "))
        m = float(input("Enter first ratio: "))
        n = float(input("Enter second ratio: "))

        if length <= 0 or m <= 0 or n <= 0:
            print("All values must be positive.")
            return

        first = length * m / (m + n)
        second = length * n / (m + n)

        print("First Segment Length =", round(first, 2))
        print("Second Segment Length =", round(second, 2))

    elif choice == "2":
        first = float(input("Enter first segment length: "))
        second = float(input("Enter second segment length: "))

        if first <= 0 or second <= 0:
            print("Segment lengths must be positive.")
            return

        print("Segment Ratio =", round(first / second, 4), ": 1")

    elif choice == "3":
        x1 = float(input("Enter x-coordinate of first point: "))
        y1 = float(input("Enter y-coordinate of first point: "))
        x2 = float(input("Enter x-coordinate of second point: "))
        y2 = float(input("Enter y-coordinate of second point: "))
        m = float(input("Enter first ratio: "))
        n = float(input("Enter second ratio: "))

        if m <= 0 or n <= 0:
            print("Ratio values must be positive.")
            return

        x = (m * x2 + n * x1) / (m + n)
        y = (m * y2 + n * y1) / (m + n)

        print("Division Point =", (round(x, 2), round(y, 2)))

    else:
        print("Invalid choice.")

linesegmentratiodivider()