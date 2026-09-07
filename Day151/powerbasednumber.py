def powerbasednumber():
    print("Power-Based Number Representation :")

    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    print("\nChoose representation:")
    print("1. Base-2 (Powers of 2)")
    print("2. Base-3 (Powers of 3)")
    print("3. Base-10 (Powers of 10)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        base = 2
    elif choice == 2:
        base = 3
    elif choice == 3:
        base = 10
    else:
        print("Invalid choice.")
        return

    original = number
    terms = []

    exponent = 0

    while number > 0:
        digit = number % base

        if digit != 0:
            terms.append((digit, exponent))

        number //= base
        exponent += 1

    print("\nPower-Based Representation :")
    print("Number:", original)
    print("Base:", base)

    expression = []

    for coefficient, exponent in reversed(terms):
        if exponent == 0:
            expression.append(str(coefficient))
        elif coefficient == 1:
            expression.append(f"{base}^{exponent}")
        else:
            expression.append(f"{coefficient} × {base}^{exponent}")

    print("Representation:", " + ".join(expression))

powerbasednumber()