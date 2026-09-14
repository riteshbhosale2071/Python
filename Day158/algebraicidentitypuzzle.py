def algebraicidentitypuzzle():
    print("Algebraic Identity Puzzle Generator :")
    print("1. Square of Sum")
    print("2. Square of Difference")
    print("3. Difference of Squares")

    choice = int(input("Choose a puzzle: "))

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if choice == 1:
        answer = a * a + 2 * a * b + b * b
        print("Puzzle: (", a, "+", b, ")^2")
        print("Answer =", answer)

    elif choice == 2:
        answer = a * a - 2 * a * b + b * b
        print("Puzzle: (", a, "-", b, ")^2")
        print("Answer =", answer)

    elif choice == 3:
        answer = (a + b) * (a - b)
        print("Puzzle:", a, "^2 -", b, "^2")
        print("Answer =", answer)

    else:
        print("Invalid choice.")

algebraicidentitypuzzle()