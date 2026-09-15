def factorexpansioncross():
    print("Factor Expansion Cross-Checker :")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    print("Choose expression:")
    print("1. (a + b)(a - b)")
    print("2. (a + b)^2")
    print("3. (a - b)^2")

    choice = int(input("Enter choice: "))

    if choice == 1:
        factor_form = (a + b) * (a - b)
        expanded_form = a * a - b * b

    elif choice == 2:
        factor_form = (a + b) * (a + b)
        expanded_form = a * a + 2 * a * b + b * b

    elif choice == 3:
        factor_form = (a - b) * (a - b)
        expanded_form = a * a - 2 * a * b + b * b

    else:
        print("Invalid choice.")
        return

    print("Factor form value =", factor_form)
    print("Expanded form value =", expanded_form)

    if factor_form == expanded_form:
        print("Cross-check successful. Both forms are equivalent.")
    else:
        print("Cross-check failed. The forms are not equivalent.")

factorexpansioncross()