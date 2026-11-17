def multiplemethodquadratic():
    print("Multiple Method Quadratic Solver")

    print("\nEnter coefficients of ax² + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient a cannot be zero.")
        return

    discriminant = b ** 2 - 4 * a * c

    print("\n1. Quadratic Formula Method")
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print("Root 1:", round(root1, 2))
        print("Root 2:", round(root2, 2))

    elif discriminant == 0:
        root = -b / (2 * a)
        print("Repeated Root:", round(root, 2))

    else:
        real = -b / (2 * a)
        imaginary = (-discriminant) ** 0.5 / abs(2 * a)
        print(f"Complex Roots: {real:.2f} + {imaginary:.2f}i")
        print(f"               {real:.2f} - {imaginary:.2f}i")

    print("\n2. Discriminant Method")
    print("Discriminant:", discriminant)

    if discriminant > 0:
        print("Two distinct real roots.")
    elif discriminant == 0:
        print("Two equal real roots.")
    else:
        print("Two complex roots.")

    print("\n3. Sum and Product of Roots Method")
    sum_roots = -b / a
    product_roots = c / a

    print("Sum of Roots:", round(sum_roots, 2))
    print("Product of Roots:", round(product_roots, 2))

    print("\n4. Completing the Square Method")
    print("Divide equation by a and calculate the roots using:")
    print("x = -b/(2a) ± √(b² - 4ac)/(2a)")

multiplemethodquadratic()