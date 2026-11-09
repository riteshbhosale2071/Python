def discriminantcalculator():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Invalid quadratic equation. Coefficient a cannot be zero.")
            return

        discriminant = b ** 2 - 4 * a * c

        print("Discriminant:", discriminant)

        if discriminant > 0:
            print("Two distinct real roots.")
        elif discriminant == 0:
            print("Two equal real roots.")
        else:
            print("Two complex roots.")

    except ValueError:
        print("Please enter valid numeric values.")

discriminantcalculator()