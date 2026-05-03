calc = {
    1: ("Addition", lambda a, b: a + b),
    2: ("Subtraction", lambda a, b: a - b),
    3: ("Multiplication", lambda a, b: a * b),
    4: ("Division", lambda a, b: a / b if b != 0 else "Cannot divide by zero")
}
while True:
    print("\nCalculator Menu")
    for key, value in calc.items():
        print(f"{key}. {value[0]}")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting...")
        break
    if choice in calc:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = calc[choice][1](a, b)
        print("Result:", result)
    else:
        print("Invalid choice, try again")