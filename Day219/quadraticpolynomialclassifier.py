def quadraticpolynomialclassifier():
    print("Quadratic Polynomial Classifier")
    print("Standard Form: ax² + bx + c")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("This is not a quadratic polynomial.")
        if b != 0:
            print("It is a linear polynomial.")
        elif c != 0:
            print("It is a constant polynomial.")
        else:
            print("It is a zero polynomial.")
        return

    print("\nPolynomial: {}x² + {}x + {}".format(a, b, c))
    print("Degree: 2")

    if b == 0 and c == 0:
        print("Classification: Pure quadratic polynomial.")
    elif b == 0:
        print("Classification: Quadratic binomial without a linear term.")
    elif c == 0:
        print("Classification: Quadratic binomial without a constant term.")
    else:
        print("Classification: Complete quadratic trinomial.")

    if a > 0:
        print("Leading coefficient is positive.")
    else:
        print("Leading coefficient is negative.")

quadraticpolynomialclassifier()