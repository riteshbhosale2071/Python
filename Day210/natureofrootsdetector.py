def natureofrootsdetector():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation.")
            return

        discriminant = b ** 2 - 4 * a * c

        print("Discriminant:", discriminant)

        if discriminant > 0:
            print("Nature of Roots: Two distinct real roots")

            if discriminant > 0:
                print("Roots are irrational if the discriminant is not a perfect square.")

        elif discriminant == 0:
            print("Nature of Roots: Two equal real roots")
            print("Roots are real and rational.")

        else:
            print("Nature of Roots: Two distinct complex conjugate roots")
            print("Roots are imaginary.")

    except ValueError:
        print("Please enter valid numeric coefficients.")

natureofrootsdetector()