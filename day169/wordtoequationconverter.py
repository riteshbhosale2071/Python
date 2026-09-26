def wordtoequationconverter():
    print("Word-to-Equation Converter :")

    number_of_problems = int(input("Enter the number of problems: "))

    if number_of_problems <= 0:
        print("Number of problems must be greater than zero.")
        return

    for i in range(number_of_problems):
        print("\nProblem", i + 1, ":")
        print("1. A number plus a value")
        print("2. A number minus a value")
        print("3. A number multiplied by a value")
        print("4. A number divided by a value")

        choice = int(input("Enter your choice: "))
        value = float(input("Enter the value: "))
        result = float(input("Enter the result: "))

        if choice == 1:
            print("Word Statement: A number plus", value, "equals", result)
            print("Equation: x +", value, "=", result)

        elif choice == 2:
            print("Word Statement: A number minus", value, "equals", result)
            print("Equation: x -", value, "=", result)

        elif choice == 3:
            print("Word Statement:", value, "times a number equals", result)
            print("Equation:", value, "x =", result)

        elif choice == 4:
            if value == 0:
                print("Division by zero is not allowed.")
            else:
                print("Word Statement: A number divided by", value, "equals", result)
                print("Equation: x /", value, "=", result)

        else:
            print("Invalid choice.")

    print("\nWord-to-Equation Conversion Completed.")

wordtoequationconverter()