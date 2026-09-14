def identityequivalencechecker():
    print("Identity Equivalence Checker :")
    print("1. (a + b)^2 and a^2 + 2ab + b^2")
    print("2. (a - b)^2 and a^2 - 2ab + b^2")
    print("3. (a + b)(a - b) and a^2 - b^2")

    choice = int(input("Choose an identity: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        left = (a + b) * (a + b)
        right = a * a + 2 * a * b + b * b

    elif choice == 2:
        left = (a - b) * (a - b)
        right = a * a - 2 * a * b + b * b

    elif choice == 3:
        left = (a + b) * (a - b)
        right = a * a - b * b

    else:
        print("Invalid choice.")
        return

    print("Left side =", left)
    print("Right side =", right)

    if left == right:
        print("The expressions are equivalent.")
    else:
        print("The expressions are not equivalent.")

identityequivalencechecker()