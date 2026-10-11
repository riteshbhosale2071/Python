def compositeareachallenge():
    print("Composite Area Challenge :")
    print("Solve the area problems and check your answers!")

    score = 0

    print("\nChallenge 1: Rectangle with a triangular top")
    length = 10
    width = 6
    base = 10
    height = 4

    correct_answer = (length * width) + (0.5 * base * height)
    print("Rectangle: Length =", length, ", Width =", width)
    print("Triangle: Base =", base, ", Height =", height)
    answer = float(input("Enter the total area: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect. Correct area:", correct_answer)

    print("\nChallenge 2: Rectangle with a semicircle")
    length = 8
    width = 6
    radius = 3

    correct_answer = (length * width) + (0.5 * 3.14159 * radius * radius)
    print("Rectangle: Length =", length, ", Width =", width)
    print("Semicircle radius =", radius)
    answer = float(input("Enter the total area: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect. Correct area:", round(correct_answer, 2))

    print("\nChallenge 3: Large rectangle with a smaller rectangle removed")
    outer_length = 12
    outer_width = 9
    inner_length = 4
    inner_width = 3

    correct_answer = (outer_length * outer_width) - (inner_length * inner_width)
    print("Outer rectangle: Length =", outer_length, ", Width =", outer_width)
    print("Removed rectangle: Length =", inner_length, ", Width =", inner_width)
    answer = float(input("Enter the remaining area: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect. Correct area:", correct_answer)

    print("\nFinal Results :")
    print("Score:", score, "out of 3")

    if score == 3:
        print("Excellent! You solved every challenge.")
    elif score == 2:
        print("Good work! Keep practicing.")
    elif score == 1:
        print("Nice attempt! Review the area formulas.")
    else:
        print("Keep practicing. You will improve!")

compositeareachallenge()