def mathematicalexpressionsimplification():
    print("Mathematical Expression Simplification :")
    print("1. Combine Like Terms")
    print("2. Simplify Fraction")
    print("3. Simplify Percentage")
    print("4. Evaluate Expression")

    choice = int(input("Select an operation: "))

    if choice == 1:
        coefficient1 = float(input("Enter coefficient of x in first term: "))
        coefficient2 = float(input("Enter coefficient of x in second term: "))
        constant1 = float(input("Enter first constant: "))
        constant2 = float(input("Enter second constant: "))

        coefficient = coefficient1 + coefficient2
        constant = constant1 + constant2

        print("\nSimplified Expression :")

        if coefficient != 0 and constant != 0:
            print("Expression:", coefficient, "x +", constant)
        elif coefficient != 0:
            print("Expression:", coefficient, "x")
        elif constant != 0:
            print("Expression:", constant)
        else:
            print("Expression: 0")

    elif choice == 2:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        if denominator == 0:
            print("Denominator cannot be zero.")
            return

        a = abs(numerator)
        b = abs(denominator)

        while b != 0:
            remainder = a % b
            a = b
            b = remainder

        simplified_numerator = numerator // a
        simplified_denominator = denominator // a

        print("\nSimplified Fraction :")
        print("Fraction:", simplified_numerator, "/", simplified_denominator)

    elif choice == 3:
        value = float(input("Enter value: "))
        percentage = float(input("Enter percentage: "))

        if percentage < 0:
            print("Percentage cannot be negative.")
            return

        result = value * percentage / 100

        print("\nSimplified Percentage :")
        print(percentage, "% of", value, "=", round(result, 2))

    elif choice == 4:
        expression = input("Enter mathematical expression: ")

        try:
            result = eval(expression, {"__builtins__": None}, {})
            print("\nResult :")
            print("Expression:", expression)
            print("Simplified Result:", result)
        except:
            print("Invalid mathematical expression.")

    else:
        print("Invalid choice.")

mathematicalexpressionsimplification()