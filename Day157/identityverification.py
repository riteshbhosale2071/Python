def identityverification():
    print("Identity Verification Engine :")

    print("1. (a + b)^2 = a^2 + 2ab + b^2")
    print("2. (a - b)^2 = a^2 - 2ab + b^2")
    print("3. a^2 - b^2 = (a + b)(a - b)")
    print("4. (a + b)(a - b) = a^2 - b^2")

    choice = int(input("\nEnter identity number: "))

    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    if choice == 1:
        left = (a + b) ** 2
        right = a ** 2 + 2 * a * b + b ** 2

    elif choice == 2:
        left = (a - b) ** 2
        right = a ** 2 - 2 * a * b + b ** 2

    elif choice == 3:
        left = a ** 2 - b ** 2
        right = (a + b) * (a - b)

    elif choice == 4:
        left = (a + b) * (a - b)
        right = a ** 2 - b ** 2

    else:
        print("Invalid identity number.")
        return

    print("\nVerification Result :")
    print("Left side:", left)
    print("Right side:", right)

    if left == right:
        print("Identity verified successfully.")
    else:
        print("Identity is not verified.")

identityverification()