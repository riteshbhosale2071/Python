def quadraticrootrelationship():
    print("Quadratic Root Relationship Analyzer")

    print("\nEnter coefficients of ax² + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient a cannot be zero.")
        return

    discriminant = b ** 2 - 4 * a * c

    sum_roots = -b / a
    product_roots = c / a

    print("\nQuadratic Equation:", f"{a}x² + {b}x + {c} = 0")
    print("Discriminant:", discriminant)
    print("Sum of Roots:", round(sum_roots, 2))
    print("Product of Roots:", round(product_roots, 2))

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)

        print("\nRoots are real and distinct.")
        print("Root 1:", round(root1, 2))
        print("Root 2:", round(root2, 2))

    elif discriminant == 0:
        root1 = -b / (2 * a)
        root2 = root1

        print("\nRoots are real and equal.")
        print("Root 1:", round(root1, 2))
        print("Root 2:", round(root2, 2))

    else:
        real = -b / (2 * a)
        imaginary = (-discriminant) ** 0.5 / abs(2 * a)

        print("\nRoots are complex conjugates.")
        print(f"Root 1: {real:.2f} + {imaginary:.2f}i")
        print(f"Root 2: {real:.2f} - {imaginary:.2f}i")

    print("\nVerification:")
    print("Sum of Roots × a + b:", round(a * sum_roots + b, 2))
    print("Product of Roots × a - c:", round(a * product_roots - c, 2))

quadraticrootrelationship()