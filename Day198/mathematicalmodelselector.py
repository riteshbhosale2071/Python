def mathematicalmodelselector():
    print("MATHEMATICAL MODEL SELECTOR :")

    print("\nSelect the type of problem you want to model:")
    print("1. Linear Model")
    print("2. Quadratic Model")
    print("3. Exponential Growth Model")
    print("4. Exponential Decay Model")
    print("5. Proportional Model")
    print("6. Inverse Proportional Model")
    print("7. Distance-Speed-Time Model")
    print("8. Simple Interest Model")
    print("9. Compound Interest Model")
    print("10. Arithmetic Sequence Model")

    choice = input("\nEnter your choice (1-10): ").strip()

    def get_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return None

    if choice == "1":
        print("LINEAR MODEL: y = mx + c")
        m = get_number("Enter slope (m): ")
        if m is None:
            return
        c = get_number("Enter intercept (c): ")
        if c is None:
            return
        x = get_number("Enter x value: ")
        if x is None:
            return

        y = m * x + c
        print("\nSelected Model: Linear")
        print(f"Equation: y = {m}x + {c}")
        print("Calculated y =", y)

    elif choice == "2":
        print("QUADRATIC MODEL: y = ax² + bx + c")
        a = get_number("Enter coefficient a: ")
        if a is None:
            return
        b = get_number("Enter coefficient b: ")
        if b is None:
            return
        c = get_number("Enter constant c: ")
        if c is None:
            return
        x = get_number("Enter x value: ")
        if x is None:
            return

        if a == 0:
            print("Coefficient a must not be zero for a quadratic model.")
            return

        y = a * x ** 2 + b * x + c
        discriminant = b ** 2 - 4 * a * c

        print("\nSelected Model: Quadratic")
        print(f"Equation: y = {a}x² + {b}x + {c}")
        print("Calculated y =", y)
        print("Discriminant =", discriminant)

        if discriminant > 0:
            print("The equation has two distinct real roots.")
        elif discriminant == 0:
            print("The equation has one repeated real root.")
        else:
            print("The equation has no real roots.")

    elif choice in ["3", "4"]:
        initial = get_number("Enter initial value: ")
        if initial is None:
            return
        rate = get_number("Enter rate percentage: ")
        if rate is None:
            return
        time = get_number("Enter time period: ")
        if time is None:
            return

        if initial < 0 or time < 0 or rate < 0:
            print("Initial value, rate, and time must be non-negative.")
            return

        if choice == "3":
            result = initial * (1 + rate / 100) ** time
            model = "Exponential Growth"
        else:
            result = initial * (1 - rate / 100) ** time
            model = "Exponential Decay"

            if rate > 100:
                print("Decay rate cannot exceed 100%.")
                return

        print("\nSelected Model:", model)
        print("Initial Value:", initial)
        print("Rate:", rate, "%")
        print("Time:", time)
        print("Final Value:", round(result, 4))

    elif choice == "5":
        print("PROPORTIONAL MODEL: y = kx")
        k = get_number("Enter proportionality constant (k): ")
        if k is None:
            return
        x = get_number("Enter x value: ")
        if x is None:
            return

        y = k * x
        print("\nSelected Model: Direct Proportion")
        print("Equation: y =", k, "*", x)
        print("Calculated y =", y)

    elif choice == "6":
        print("INVERSE PROPORTION MODEL: y = k/x")
        k = get_number("Enter constant (k): ")
        if k is None:
            return
        x = get_number("Enter x value: ")
        if x is None:
            return

        if x == 0:
            print("x cannot be zero.")
            return

        y = k / x
        print("\nSelected Model: Inverse Proportion")
        print("Calculated y =", y)

    elif choice == "7":
        print("DISTANCE MODEL: Distance = Speed × Time")
        print("1. Calculate distance")
        print("2. Calculate speed")
        print("3. Calculate time")

        subchoice = input("Choose an operation (1-3): ").strip()

        if subchoice == "1":
            speed = get_number("Enter speed: ")
            if speed is None:
                return
            time = get_number("Enter time: ")
            if time is None:
                return
            if speed < 0 or time < 0:
                print("Speed and time must be non-negative.")
                return
            print("Distance =", speed * time)

        elif subchoice == "2":
            distance = get_number("Enter distance: ")
            if distance is None:
                return
            time = get_number("Enter time: ")
            if time is None:
                return
            if distance < 0 or time <= 0:
                print("Distance must be non-negative and time positive.")
                return
            print("Speed =", distance / time)

        elif subchoice == "3":
            distance = get_number("Enter distance: ")
            if distance is None:
                return
            speed = get_number("Enter speed: ")
            if speed is None:
                return
            if distance < 0 or speed <= 0:
                print("Distance must be non-negative and speed positive.")
                return
            print("Time =", distance / speed)

        else:
            print("Invalid operation.")
            return

    elif choice == "8":
        print("SIMPLE INTEREST MODEL: SI = P × R × T / 100")
        principal = get_number("Enter principal amount: ")
        if principal is None:
            return
        rate = get_number("Enter annual interest rate (%): ")
        if rate is None:
            return
        time = get_number("Enter time in years: ")
        if time is None:
            return

        if principal < 0 or rate < 0 or time < 0:
            print("Inputs must be non-negative.")
            return

        interest = principal * rate * time / 100
        print("\nSimple Interest =", round(interest, 2))
        print("Total Amount =", round(principal + interest, 2))

    elif choice == "9":
        print("COMPOUND INTEREST MODEL: A = P(1 + R/100)^T")
        principal = get_number("Enter principal amount: ")
        if principal is None:
            return
        rate = get_number("Enter annual interest rate (%): ")
        if rate is None:
            return
        time = get_number("Enter time in years: ")
        if time is None:
            return

        if principal < 0 or rate < 0 or time < 0:
            print("Inputs must be non-negative.")
            return

        amount = principal * (1 + rate / 100) ** time
        interest = amount - principal

        print("\nCompound Interest =", round(interest, 2))
        print("Final Amount =", round(amount, 2))

    elif choice == "10":
        print("ARITHMETIC SEQUENCE MODEL: an = a1 + (n-1)d")
        first = get_number("Enter first term: ")
        if first is None:
            return
        difference = get_number("Enter common difference: ")
        if difference is None:
            return

        try:
            n = int(input("Enter term number n: "))
        except ValueError:
            print("Term number must be an integer.")
            return

        if n <= 0:
            print("Term number must be positive.")
            return

        term = first + (n - 1) * difference
        total = n * (2 * first + (n - 1) * difference) / 2

        print("\nSelected Model: Arithmetic Sequence")
        print("Nth Term =", term)
        print("Sum of First", n, "Terms =", total)

    else:
        print("Invalid choice! Select a model from 1 to 10.")
        return

    print("\nModel evaluation completed successfully.")

mathematicalmodelselector()