def factorisationchallenge():
    print("Factorisation Challenge Generator :")
    print("1. Common Factor")
    print("2. Difference of Squares")
    print("3. Perfect Square")

    choice = int(input("Choose challenge type: "))

    if choice == 1:
        common = int(input("Enter common factor: "))
        a = int(input("Enter first multiplier: "))
        b = int(input("Enter second multiplier: "))

        term1 = common * a
        term2 = common * b

        print("Challenge:", term1, "x +", term2, "x")
        print("Find the common factor.")

        answer = int(input("Enter your answer: "))

        if answer == common:
            print("Correct!")
        else:
            print("Incorrect. Correct answer =", common)

    elif choice == 2:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        expression = a * a - b * b

        print("Challenge:", expression)
        print("Factorise the expression.")

        answer = int(input("Enter first factor: "))
        second = int(input("Enter second factor: "))

        if answer * second == expression:
            print("Correct factorisation!")
        else:
            print("Incorrect factorisation.")

    elif choice == 3:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        first = a * a
        middle = 2 * a * b
        last = b * b

        print("Challenge:", first, "+", middle, "x +", last)
        print("Find the value of a + b.")

        answer = int(input("Enter your answer: "))

        if answer == a + b:
            print("Correct!")
        else:
            print("Incorrect. Correct answer =", a + b)

    else:
        print("Invalid choice.")

factorisationchallenge()