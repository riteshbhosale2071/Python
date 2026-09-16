def factorisationmatching():
    print("Factorisation Matching Game :")
    print("Match the expression with its factorised form.")
    print("1. x^2 - 25")
    print("2. x^2 + 10x + 25")
    print("3. x^2 - 10x + 25")

    print("A. (x - 5)(x - 5)")
    print("B. (x + 5)(x + 5)")
    print("C. (x + 5)(x - 5)")

    score = 0

    answer = input("Match 1 with A, B, or C: ").upper()
    if answer == "C":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    answer = input("Match 2 with A, B, or C: ").upper()
    if answer == "B":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    answer = input("Match 3 with A, B, or C: ").upper()
    if answer == "A":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    print("Your score =", score, "out of 3")

factorisationmatching()