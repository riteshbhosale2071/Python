def algebraicsquareexpansion():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))

    choice = input("Enter expression type (+ for (a+b)^2, - for (a-b)^2): ")

    if choice == "+":
        result = a ** 2 + 2 * a * b + b ** 2
        print("Expansion: a² + 2ab + b²")
        print("Result:", result)

    elif choice == "-":
        result = a ** 2 - 2 * a * b + b ** 2
        print("Expansion: a² - 2ab + b²")
        print("Result:", result)

    else:
        print("Invalid choice.")

algebraicsquareexpansion()