def quadraticequationvalidator():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation. Coefficient a cannot be zero.")
            return

        discriminant = b ** 2 - 4 * a * c

        print("\nEquation: ax² + bx + c = 0")
        print("Discriminant:", discriminant)

        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)

            print("Result: Two distinct real roots")
            print("Root 1:", round(root1, 4))
            print("Root 2:", round(root2, 4))

        elif discriminant == 0:
            root = -b / (2 * a)

            print("Result: Two equal real roots")
            print("Root:", round(root, 4))

        else:
            real = -b / (2 * a)
            imaginary = (abs(discriminant) ** 0.5) / abs(2 * a)

            print("Result: Two complex roots")
            print(f"Root 1: {real:.4f} + {imaginary:.4f}i")
            print(f"Root 2: {real:.4f} - {imaginary:.4f}i")

        print("Validation: Valid quadratic equation.")

    except ValueError:
        print("Please enter valid numeric coefficients.")

quadraticequationvalidator()