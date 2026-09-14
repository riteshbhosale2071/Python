def mathstrainer():
    print("Identity-Based Mental Maths Trainer :")
    print("1. Square of a number")
    print("2. Difference of squares")
    print("3. Product using (a + b)(a - b)")

    choice = int(input("Choose a question: "))

    if choice == 1:
        number = int(input("Enter a number: "))
        base = (number // 10) * 10
        difference = number - base
        answer = base * base + 2 * base * difference + difference * difference
        print("Using (a + b)^2")
        print("Answer =", answer)

    elif choice == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        answer = (a + b) * (a - b)
        print("Using a^2 - b^2")
        print("Answer =", answer)

    elif choice == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        answer = a * a - b * b
        print("Using (a + b)(a - b) = a^2 - b^2")
        print("Answer =", answer)

    else:
        print("Invalid choice.")

mathstrainer()