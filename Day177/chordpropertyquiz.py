def chordpropertyquiz():
    print("Chord Property Quiz Generator :")

    score = 0

    print("\nQuestion 1:")
    print("What happens when a perpendicular is drawn from the center of a circle to a chord?")
    print("1. It doubles the chord")
    print("2. It bisects the chord")
    print("3. It becomes parallel to the chord")
    print("4. It removes the chord")

    answer = int(input("Enter your answer: "))

    if answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 2.")

    print("\nQuestion 2:")
    print("What is the longest chord of a circle?")
    print("1. Radius")
    print("2. Minor chord")
    print("3. Diameter")
    print("4. Arc")

    answer = int(input("Enter your answer: "))

    if answer == 3:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 3.")

    print("\nQuestion 3:")
    print("Two chords are equally distant from the center of a circle. What can be concluded?")
    print("1. They have equal lengths")
    print("2. One chord is always a diameter")
    print("3. They have different lengths")
    print("4. They cannot exist in the same circle")

    answer = int(input("Enter your answer: "))

    if answer == 1:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 1.")

    print("\nQuestion 4:")
    print("If two chords of the same circle have equal lengths, how are they related to the center?")
    print("1. They are equally distant from the center")
    print("2. One must pass through the center")
    print("3. They must be perpendicular")
    print("4. They must have different distances")

    answer = int(input("Enter your answer: "))

    if answer == 1:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 1.")

    print("\nQuestion 5:")
    print("What is the midpoint of a diameter relative to the circle?")
    print("1. On the circumference")
    print("2. At the center")
    print("3. Outside the circle")
    print("4. On an arc")

    answer = int(input("Enter your answer: "))

    if answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 2.")

    print("\nQuiz Result :")
    print("Score:", score, "out of 5")

    if score == 5:
        print("Excellent! Perfect score.")
    elif score >= 3:
        print("Good job! Keep practicing.")
    else:
        print("Keep practicing chord properties.")

chordpropertyquiz()