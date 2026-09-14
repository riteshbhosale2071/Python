def identitytransformation():
    print("Identity Transformation Program :")
    print("1. a^2 + 2ab + b^2")
    print("2. a^2 - 2ab + b^2")
    print("3. a^2 - b^2")

    choice = int(input("Enter expression choice: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        result = (a + b) * (a + b)
        print("Transformed form =", result)

    elif choice == 2:
        result = (a - b) * (a - b)
        print("Transformed form =", result)

    elif choice == 3:
        result = (a + b) * (a - b)
        print("Transformed form =", result)

    else:
        print("Invalid choice.")

identitytransformation()