def quadraticrootcalculator():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation.")
            return

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)

            print("Root 1:", round(root1, 4))
            print("Root 2:", round(root2, 4))
            print("Type: Two distinct real roots")

        elif discriminant == 0:
            root = -b / (2 * a)

            print("Root 1:", round(root, 4))
            print("Root 2:", round(root, 4))
            print("Type: Two equal real roots")

        else:
            real = -b / (2 * a)
            imaginary = (-discriminant) ** 0.5 / abs(2 * a)

            print(f"Root 1: {real:.4f} + {imaginary:.4f}i")
            print(f"Root 2: {real:.4f} - {imaginary:.4f}i")
            print("Type: Two complex roots")

    except ValueError:
        print("Please enter valid numeric coefficients.")

quadraticrootcalculator()