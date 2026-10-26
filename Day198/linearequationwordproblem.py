def linearequationwordproblem():
    print("LINEAR EQUATION WORD-PROBLEM CONVERTER :")

    def solve_equation(a, b, c):
        if a == 0:
            if b == c:
                return "Infinite solutions"
            return "No solution"

        return (c - b) / a

    def display_equation(a, b, c, variable="x"):
        if b < 0:
            equation = f"{a}{variable} - {abs(b)} = {c}"
        else:
            equation = f"{a}{variable} + {b} = {c}"

        return equation

    def get_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return None

    print("\nChoose a word-problem category:")
    print("1. Number problem")
    print("2. Age problem")
    print("3. Shopping problem")
    print("4. Distance problem")
    print("5. Rectangle perimeter problem")
    print("6. Custom linear equation")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        print("\nExample: Five more than twice a number is 21.")
        a = 2
        b = 5
        c = 21
        variable = "x"
        description = "Find the unknown number."

    elif choice == "2":
        print("\nExample: A person's age plus 8 is 25.")
        a = 1
        b = 8
        c = 25
        variable = "x"
        description = "Find the person's present age."

    elif choice == "3":
        print("\nExample: Three identical notebooks and a ₹10 pen")
        print("cost ₹100 in total.")
        a = 3
        b = 10
        c = 100
        variable = "x"
        description = "Find the price of one notebook."

    elif choice == "4":
        print("\nExample: A vehicle travels at 60 km/h.")
        print("Its distance is 180 km.")
        a = 60
        b = 0
        c = 180
        variable = "t"
        description = "Find the travel time in hours."

    elif choice == "5":
        print("\nExample: A rectangle has width x and length x + 5.")
        print("Its perimeter is 30 units.")
        a = 4
        b = 10
        c = 30
        variable = "x"
        description = "Find the width of the rectangle."

    elif choice == "6":
        print("\nEnter an equation in the form ax + b = c.")
        a = get_number("Enter coefficient a: ")
        if a is None:
            return

        b = get_number("Enter constant b: ")
        if b is None:
            return

        c = get_number("Enter right-hand side c: ")
        if c is None:
            return

        variable = "x"
        description = "Solve the custom linear equation."

    else:
        print("Invalid choice. Please select 1 to 6.")
        return

    equation = display_equation(a, b, c, variable)

    print("\n" + "-" * 50)
    print("WORD-PROBLEM DETAILS")
    print("-" * 50)

    if choice != "6":
        print(description)
        print("Equation:", equation)
    else:
        print("Converted Equation:", equation)

    solution = solve_equation(a, b, c)

    print("\n" + "-" * 50)
    print("SOLUTION")
    print("-" * 50)

    if isinstance(solution, str):
        print(solution)
        return

    print("Step 1: Start with the equation:")
    print(equation)

    if b != 0:
        print("\nStep 2: Subtract", b, "from both sides.")
        print(f"{a}{variable} = {c - b}")
    else:
        print("\nStep 2: The equation has no constant to move.")

    print("\nStep 3: Divide both sides by", a)
    print(f"{variable} = ({c} - ({b})) / {a}")
    print(f"{variable} = {solution:g}")

    print("\nFinal Answer:", variable, "=", solution)

    if choice == "2" and solution < 0:
        print("Note: A negative age is not realistic.")
    elif choice == "3" and solution < 0:
        print("Note: A negative price is not realistic.")
    elif choice == "4" and solution < 0:
        print("Note: A negative travel time is not realistic.")
    elif choice == "5" and solution <= 0:
        print("Note: A rectangle's width must be positive.")

    print("\nVerification:")
    left_side = a * solution + b
    print(f"{a} * {solution:g} + ({b}) = {left_side:g}")
    print("Right-hand side =", c)

    if abs(left_side - c) < 1e-9:
        print("Verification successful!")
    else:
        print("Verification failed.")

    print("\nWord-problem conversion completed successfully.")

linearequationwordproblem()