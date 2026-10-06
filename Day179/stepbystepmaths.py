def stepbystepmaths():
    print("Step-by-Step Maths :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Simple Equation")

    choice = int(input("Select a problem type: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a + b

        print("\nStep 1:", a, "+", b)
        print("Step 2: Add the two numbers.")
        print("Answer:", round(result, 2))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a - b

        print("\nStep 1:", a, "-", b)
        print("Step 2: Subtract the second number from the first.")
        print("Answer:", round(result, 2))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a * b

        print("\nStep 1:", a, "×", b)
        print("Step 2: Multiply the two numbers.")
        print("Answer:", round(result, 2))

    elif choice == 4:
        a = float(input("Enter dividend: "))
        b = float(input("Enter divisor: "))

        if b == 0:
            print("Division by zero is not allowed.")
            return

        result = a / b

        print("\nStep 1:", a, "÷", b)
        print("Step 2: Divide the dividend by the divisor.")
        print("Answer:", round(result, 2))

    elif choice == 5:
        value = float(input("Enter value: "))
        percentage = float(input("Enter percentage: "))

        result = value * percentage / 100

        print("\nStep 1: Convert percentage to a fraction.")
        print("Step 2:", value, "×", percentage, "/ 100")
        print("Step 3: Calculate the result.")
        print("Answer:", round(result, 2))

    elif choice == 6:
        print("\nEquation format: ax + b = c")

        a = float(input("Enter coefficient of x: "))
        b = float(input("Enter constant: "))
        c = float(input("Enter right-side value: "))

        if a == 0:
            if b == c:
                print("The equation has infinitely many solutions.")
            else:
                print("The equation has no solution.")
            return

        print("\nStep 1:", a, "x +", b, "=", c)

        new_value = c - b

        print("Step 2: Subtract", b, "from both sides.")
        print(a, "x =", new_value)

        result = new_value / a

        print("Step 3: Divide both sides by", a)
        print("x =", round(result, 2))

        print("Answer: x =", round(result, 2))

    else:
        print("Invalid problem type.")

stepbystepmaths()