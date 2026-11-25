def slopeofalinecalculator():
    print("Slope of a Line Calculator")
    print("1. Calculate Slope Using Two Points")
    print("2. Calculate Slope Using Line Equation")
    print("3. Identify Line Type")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if x2 == x1:
            print("Slope is undefined (vertical line).")
            return

        slope = (y2 - y1) / (x2 - x1)
        print("Slope =", round(slope, 4))

    elif choice == "2":
        a = float(input("Enter coefficient of x (A): "))
        b = float(input("Enter coefficient of y (B): "))
        c = float(input("Enter constant (C) in Ax + By + C = 0: "))

        if b == 0:
            print("Slope is undefined (vertical line).")
            return

        slope = -a / b
        print("Slope =", round(slope, 4))

    elif choice == "3":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if x2 == x1:
            print("Vertical Line")
        else:
            slope = (y2 - y1) / (x2 - x1)

            if slope == 0:
                print("Horizontal Line")
            elif slope > 0:
                print("Positive Slope")
            else:
                print("Negative Slope")

            print("Slope =", round(slope, 4))

    else:
        print("Invalid choice.")

slopeofalinecalculator()