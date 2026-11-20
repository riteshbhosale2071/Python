def natureofrootsdetector():
    print("Nature of Roots Detector")
    print("Standard Form: ax² + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Invalid quadratic equation: a cannot be zero.")
        return

    discriminant = b ** 2 - 4 * a * c

    print("\nDiscriminant =", discriminant)

    if discriminant > 0:
        print("Nature of Roots: Two distinct real roots.")
        if discriminant.is_integer():
            root = int(discriminant ** 0.5)
            if root ** 2 == discriminant:
                print("Both roots are rational.")
            else:
                print("Both roots are irrational.")
        else:
            print("Roots may be irrational.")

    elif discriminant == 0:
        print("Nature of Roots: Two equal real roots.")
        print("Both roots are rational if a and b are rational.")

    else:
        print("Nature of Roots: Two distinct complex conjugate roots.")
        print("The equation has no real roots.")

natureofrootsdetector()