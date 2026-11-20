def discriminantcalculator():
    print("Discriminant Calculator")
    print("Standard Form: ax² + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Invalid quadratic equation: a cannot be zero.")
        return

    discriminant = b ** 2 - 4 * a * c

    print("\nDiscriminant (D) =", discriminant)

    if discriminant > 0:
        print("The equation has two distinct real roots.")
    elif discriminant == 0:
        print("The equation has two equal real roots.")
    else:
        print("The equation has two complex conjugate roots.")

discriminantcalculator()