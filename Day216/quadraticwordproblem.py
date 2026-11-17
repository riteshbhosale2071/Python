def quadraticwordproblem():
    print("Quadratic Word Problem Solver")

    print("\nSelect a problem type:")
    print("1. Area of a Rectangle")
    print("2. Product of Two Consecutive Numbers")
    print("3. Projectile Height")
    print("4. Number Problem")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        area = float(input("Enter rectangle area: "))
        difference = float(input("Enter difference between length and width: "))

        discriminant = difference ** 2 + 4 * area

        length = (difference + discriminant ** 0.5) / 2
        width = length - difference

        print("\nLength:", round(length, 2))
        print("Width:", round(width, 2))

    elif choice == 2:
        product = float(input("Enter product of two consecutive numbers: "))

        discriminant = 1 + 4 * product

        if discriminant < 0:
            print("No real solutions.")
            return

        number1 = (-1 + discriminant ** 0.5) / 2
        number2 = number1 + 1

        print("\nFirst Number:", round(number1, 2))
        print("Second Number:", round(number2, 2))

    elif choice == 3:
        initial_velocity = float(input("Enter initial velocity: "))
        time = float(input("Enter time in seconds: "))
        gravity = float(input("Enter gravity value (usually 9.8): "))

        height = initial_velocity * time - 0.5 * gravity * time ** 2

        print("\nHeight:", round(height, 2))

    elif choice == 4:
        print("\nEnter equation in the form ax² + bx + c = 0")

        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Coefficient a cannot be zero.")
            return

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)
            print("\nTwo Real Roots:", round(root1, 2), "and", round(root2, 2))

        elif discriminant == 0:
            root = -b / (2 * a)
            print("\nOne Repeated Root:", round(root, 2))

        else:
            print("\nNo Real Roots.")

    else:
        print("Invalid choice.")

quadraticwordproblem()