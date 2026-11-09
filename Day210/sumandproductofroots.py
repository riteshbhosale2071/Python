def sumandproductofroots():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation.")
            return

        sum_of_roots = -b / a
        product_of_roots = c / a

        print("\nQuadratic Equation: ax² + bx + c = 0")
        print("Sum of Roots:", round(sum_of_roots, 4))
        print("Product of Roots:", round(product_of_roots, 4))

    except ValueError:
        print("Please enter valid numeric coefficients.")

sumandproductofroots()