def factorisationpuzzle():
    print("Factorisation Puzzle Generator :")
    print("1. Common Factor")
    print("2. Difference of Squares")
    print("3. Perfect Square")

    choice = int(input("Choose puzzle type: "))

    if choice == 1:
        common = int(input("Enter common factor: "))
        a = int(input("Enter first multiplier: "))
        b = int(input("Enter second multiplier: "))

        term1 = common * a
        term2 = common * b

        print("Puzzle:", term1, "x +", term2, "x")
        print("Factorised form:", common, "x (", a, "+", b, ")")

    elif choice == 2:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        print("Puzzle:", a * a, "-", b * b)
        print("Factorised form: (", a, "+", b, ")(", a, "-", b, ")")

    elif choice == 3:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))

        first = a * a
        middle = 2 * a * b
        last = b * b

        print("Puzzle:", first, "+", middle, "x +", last)
        print("Factorised form: (", a, "x +", b, ")^2")

    else:
        print("Invalid choice.")

factorisationpuzzle()