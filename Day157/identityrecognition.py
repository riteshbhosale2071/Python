def identityrecognition():
    print("Identity Recognition Program :")

    print("1. a^2 + 2ab + b^2")
    print("2. a^2 - 2ab + b^2")
    print("3. a^2 - b^2")
    print("4. (a + b)^2")
    print("5. (a - b)^2")

    choice = int(input("\nEnter identity number: "))

    if choice == 1:
        print("Identity: (a + b)^2")
        print("Formula: a^2 + 2ab + b^2 = (a + b)^2")

    elif choice == 2:
        print("Identity: (a - b)^2")
        print("Formula: a^2 - 2ab + b^2 = (a - b)^2")

    elif choice == 3:
        print("Identity: Difference of Squares")
        print("Formula: a^2 - b^2 = (a + b)(a - b)")

    elif choice == 4:
        print("Identity: Square of a Sum")
        print("Formula: (a + b)^2 = a^2 + 2ab + b^2")

    elif choice == 5:
        print("Identity: Square of a Difference")
        print("Formula: (a - b)^2 = a^2 - 2ab + b^2")

    else:
        print("Invalid choice.")

identityrecognition()