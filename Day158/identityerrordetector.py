def identityerrordetector():
    print("Identity Error Detector :")
    print("1. (a + b)^2 = a^2 + 2ab + b^2")
    print("2. (a - b)^2 = a^2 - 2ab + b^2")
    print("3. (a + b)^2 = a^2 + b^2")
    print("4. a^2 - b^2 = (a + b)(a - b)")

    choice = int(input("Enter identity number: "))

    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    if choice == 1:
        left = (a + b) ** 2
        right = a * a + 2 * a * b + b * b

    elif choice == 2:
        left = (a - b) ** 2
        right = a * a - 2 * a * b + b * b

    elif choice == 3:
        left = (a + b) ** 2
        right = a * a + b * b

    elif choice == 4:
        left = a * a - b * b
        right = (a + b) * (a - b)

    else:
        print("Invalid identity number.")
        return

    print("\nLeft Side:", left)
    print("Right Side:", right)

    if left == right:
        print("No error detected. Identity is correct.")
    else:
        print("Error detected. Identity is incorrect.")

        if choice == 3:
            print("Correct identity: (a + b)^2 = a^2 + 2ab + b^2")

identityerrordetector()