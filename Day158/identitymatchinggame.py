def identitymatchinggame():
    print("Identity Matching Game :")

    identities = [
        ("(a + b)^2", "a^2 + 2ab + b^2"),
        ("(a - b)^2", "a^2 - 2ab + b^2"),
        ("a^2 - b^2", "(a + b)(a - b)"),
        ("(a + b)^3", "a^3 + 3a^2b + 3ab^2 + b^3"),
        ("(a - b)^3", "a^3 - 3a^2b + 3ab^2 - b^3")
    ]

    score = 0

    for i in range(len(identities)):
        print("\nQuestion", i + 1)
        print("Match this expression:")
        print(identities[i][0])

        answer = input("Enter the matching expansion: ")

        if answer.replace(" ", "").lower() == identities[i][1].replace(" ", "").lower():
            print("Correct!")
            score = score + 1
        else:
            print("Correct answer:", identities[i][1])

    print("\nGame Result :")
    print("Score:", score, "out of", len(identities))

    if score == len(identities):
        print("Perfect score!")
    elif score >= 3:
        print("Great job!")
    else:
        print("Keep practicing algebraic identities.")

identitymatchinggame()