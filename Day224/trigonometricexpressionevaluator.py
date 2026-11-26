import math

def trigonometricexpressionevaluator():
    print("Trigonometric Expression Evaluator")
    print("1. sin(x) + cos(x)")
    print("2. sin(x) * cos(x)")
    print("3. tan(x) + cot(x)")
    print("4. sec(x) + cosec(x)")
    print("5. sin²(x) + cos²(x)")
    print("6. Evaluate All Six Ratios")

    choice = input("Enter your choice (1-6): ")
    angle = float(input("Enter angle in degrees: "))
    radian = math.radians(angle)

    sine = math.sin(radian)
    cosine = math.cos(radian)

    if choice == "1":
        result = sine + cosine
    elif choice == "2":
        result = sine * cosine
    elif choice == "3":
        if math.isclose(sine, 0, abs_tol=1e-10) or math.isclose(cosine, 0, abs_tol=1e-10):
            print("Expression is undefined for this angle.")
            return
        result = sine / cosine + cosine / sine
    elif choice == "4":
        if math.isclose(sine, 0, abs_tol=1e-10) or math.isclose(cosine, 0, abs_tol=1e-10):
            print("Expression is undefined for this angle.")
            return
        result = 1 / cosine + 1 / sine
    elif choice == "5":
        result = sine ** 2 + cosine ** 2
    elif choice == "6":
        print("sin =", round(sine, 4))
        print("cos =", round(cosine, 4))
        print("tan =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else round(sine / cosine, 4))
        print("cosec =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else round(1 / sine, 4))
        print("sec =", "Undefined" if math.isclose(cosine, 0, abs_tol=1e-10) else round(1 / cosine, 4))
        print("cot =", "Undefined" if math.isclose(sine, 0, abs_tol=1e-10) else round(cosine / sine, 4))
        return
    else:
        print("Invalid choice.")
        return

    print("Expression Result =", round(result, 6))

trigonometricexpressionevaluator()