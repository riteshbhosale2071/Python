def sumandproductofrootscalc():
    print("Sum and Product of Roots Calculator")
    print("Standard Form: ax² + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Invalid quadratic equation: a cannot be zero.")
        return

    sum_roots = -b / a
    product_roots = c / a

    print("\nSum of Roots =", round(sum_roots, 4))
    print("Product of Roots =", round(product_roots, 4))

    print("\nUsing Vieta's Formulas:")
    print("Sum of roots = -b/a")
    print("Product of roots = c/a")

sumandproductofrootscalc()