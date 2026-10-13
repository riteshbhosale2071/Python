def capacityconversionchallenge():
    print("Capacity Conversion Challenge :")
    print("Convert the given capacity into the requested unit.")
    print("1. Liters to Milliliters")
    print("2. Milliliters to Liters")
    print("3. Liters to Cubic Meters")
    print("4. Cubic Meters to Liters")
    print("5. Gallons to Liters")
    print("6. Liters to Gallons")

    score = 0
    total_questions = 3

    for i in range(total_questions):
        print("\nQuestion", i + 1)
        choice = input("Select conversion type (1-6): ")

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. No point awarded.")
            continue

        value = float(input("Enter the capacity value: "))

        if value < 0:
            print("Capacity cannot be negative.")
            continue

        if choice == "1":
            correct_answer = value * 1000
            conversion = "milliliters"
        elif choice == "2":
            correct_answer = value / 1000
            conversion = "liters"
        elif choice == "3":
            correct_answer = value / 1000
            conversion = "cubic meters"
        elif choice == "4":
            correct_answer = value * 1000
            conversion = "liters"
        elif choice == "5":
            correct_answer = value * 3.78541
            conversion = "liters"
        else:
            correct_answer = value / 3.78541
            conversion = "gallons"

        answer = float(input("Enter your converted answer: "))

        if abs(answer - correct_answer) <= max(0.01, abs(correct_answer) * 0.001):
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer.")
            print("Correct result:", round(correct_answer, 4), conversion)

    print("\nChallenge Results :")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Incorrect Answers:", total_questions - score)
    print("Final Score:", str(score) + "/" + str(total_questions))
    print("Percentage:", round((score / total_questions) * 100, 2), "%")

    if score == total_questions:
        print("Excellent! Perfect score!")
    elif score >= 2:
        print("Good job! Keep practicing.")
    else:
        print("Keep practicing capacity conversions.")

capacityconversionchallenge()