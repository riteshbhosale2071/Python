def chordgeometrypuzzle():
    print("Chord Geometry Puzzle Generator :")
    print("Solve the chord geometry puzzles and check your answers!")

    import math

    score = 0
    total_questions = 3

    print("\nPuzzle 1: Find the Chord Length")
    radius = 10
    distance = 6

    correct_answer = 2 * math.sqrt(radius ** 2 - distance ** 2)

    print("Circle radius:", radius)
    print("Perpendicular distance from center to chord:", distance)
    answer = float(input("Enter the chord length: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(correct_answer, 2))

    print("\nPuzzle 2: Find the Radius")
    chord = 16
    distance = 6

    correct_answer = math.sqrt((chord / 2) ** 2 + distance ** 2)

    print("Chord length:", chord)
    print("Distance from center to chord:", distance)
    answer = float(input("Enter the circle radius: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(correct_answer, 2))

    print("\nPuzzle 3: Find the Central Angle")
    radius = 10
    chord = 10

    correct_answer = math.degrees(
        2 * math.asin(chord / (2 * radius))
    )

    print("Circle radius:", radius)
    print("Chord length:", chord)
    answer = float(input("Enter the minor central angle in degrees: "))

    if abs(answer - correct_answer) < 0.01:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(correct_answer, 2), "degrees")

    print("\nPuzzle Results :")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Incorrect Answers:", total_questions - score)
    print("Final Score:", str(score) + "/" + str(total_questions))
    print("Percentage:", round(score / total_questions * 100, 2), "%")

    if score == total_questions:
        print("Excellent! You mastered all the puzzles.")
    elif score == 2:
        print("Great work! You are almost there.")
    elif score == 1:
        print("Good attempt! Keep practicing.")
    else:
        print("Review the chord formulas and try again.")

chordgeometrypuzzle()