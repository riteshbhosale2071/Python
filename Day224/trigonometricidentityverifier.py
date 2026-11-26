import math

def trigonometricidentityverifier():
    print("Trigonometric Identity Verifier")
    print("1. Verify sin²θ + cos²θ = 1")
    print("2. Verify 1 + tan²θ = sec²θ")
    print("3. Verify 1 + cot²θ = cosec²θ")
    print("4. Verify tanθ = sinθ / cosθ")
    print("5. Verify cotθ = cosθ / sinθ")

    choice = input("Enter your choice (1-5): ")
    angle = float(input("Enter angle in degrees: "))
    radian = math.radians(angle)

    sine = math.sin(radian)
    cosine = math.cos(radian)

    if choice == "1":
        lhs = sine ** 2 + cosine ** 2
        rhs = 1

    elif choice == "2":
        if math.isclose(cosine, 0, abs_tol=1e-10):
            print("Identity is undefined for this angle.")
            return

        tangent = sine / cosine
        secant = 1 / cosine
        lhs = 1 + tangent ** 2
        rhs = secant ** 2

    elif choice == "3":
        if math.isclose(sine, 0, abs_tol=1e-10):
            print("Identity is undefined for this angle.")
            return

        cotangent = cosine / sine
        cosecant = 1 / sine
        lhs = 1 + cotangent ** 2
        rhs = cosecant ** 2

    elif choice == "4":
        if math.isclose(cosine, 0, abs_tol=1e-10):
            print("Identity is undefined for this angle.")
            return

        lhs = sine / cosine
        rhs = math.tan(radian)

    elif choice == "5":
        if math.isclose(sine, 0, abs_tol=1e-10):
            print("Identity is undefined for this angle.")
            return

        lhs = cosine / sine
        rhs = 1 / math.tan(radian)

    else:
        print("Invalid choice.")
        return

    print("LHS =", round(lhs, 6))
    print("RHS =", round(rhs, 6))

    if math.isclose(lhs, rhs, rel_tol=1e-9, abs_tol=1e-9):
        print("The trigonometric identity is verified.")
    else:
        print("The trigonometric identity is not verified.")

trigonometricidentityverifier()