def quadraticequationfactorizer():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Not a quadratic equation.")
            return

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            print("The equation cannot be factorized into real linear factors.")
            return

        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)

        print("\nQuadratic Equation:")
        print(f"{a}x² + {b}x + {c} = 0")

        if root1 == root2:
            print(f"\nFactorized Form: {a}(x - ({root1:.4f}))² = 0")
        else:
            print(f"\nFactorized Form: {a}(x - ({root1:.4f}))(x - ({root2:.4f})) = 0")

        print("\nRoots:")
        print("Root 1:", round(root1, 4))
        print("Root 2:", round(root2, 4))

    except ValueError:
        print("Please enter valid numeric coefficients.")

quadraticequationfactorizer()