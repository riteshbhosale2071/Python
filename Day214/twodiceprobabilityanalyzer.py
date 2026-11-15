def twodiceprobabilityanalyzer():
    print("Two-Dice Probability Analyzer")

    print("\nSelect an event:")
    print("1. Sum equals 2")
    print("2. Sum equals 7")
    print("3. Sum equals 12")
    print("4. Sum is even")
    print("5. Sum is odd")
    print("6. Sum is greater than 8")
    print("7. Both dice show the same number")
    print("8. Both dice show different numbers")
    print("9. Both dice show even numbers")
    print("10. Both dice show odd numbers")
    print("11. First die shows a specific number")

    choice = int(input("\nEnter your choice: "))

    sample_space = [
        (i, j)
        for i in range(1, 7)
        for j in range(1, 7)
    ]

    favorable_outcomes = []

    for die1, die2 in sample_space:
        total = die1 + die2

        if choice == 1 and total == 2:
            favorable_outcomes.append((die1, die2))
        elif choice == 2 and total == 7:
            favorable_outcomes.append((die1, die2))
        elif choice == 3 and total == 12:
            favorable_outcomes.append((die1, die2))
        elif choice == 4 and total % 2 == 0:
            favorable_outcomes.append((die1, die2))
        elif choice == 5 and total % 2 != 0:
            favorable_outcomes.append((die1, die2))
        elif choice == 6 and total > 8:
            favorable_outcomes.append((die1, die2))
        elif choice == 7 and die1 == die2:
            favorable_outcomes.append((die1, die2))
        elif choice == 8 and die1 != die2:
            favorable_outcomes.append((die1, die2))
        elif choice == 9 and die1 % 2 == 0 and die2 % 2 == 0:
            favorable_outcomes.append((die1, die2))
        elif choice == 10 and die1 % 2 != 0 and die2 % 2 != 0:
            favorable_outcomes.append((die1, die2))
        elif choice == 11:
            number = int(input("Enter a number between 1 and 6: "))
            if number not in range(1, 7):
                print("Invalid number.")
                return
            choice = 12
            for first, second in sample_space:
                if first == number:
                    favorable_outcomes.append((first, second))
            break

    if choice not in range(1, 13):
        print("Invalid choice.")
        return

    total_outcomes = len(sample_space)
    favorable_count = len(favorable_outcomes)
    probability = favorable_count / total_outcomes

    print("\nProbability Analysis :")
    print("Total Possible Outcomes:", total_outcomes)
    print("Favorable Outcomes:", favorable_count)
    print("Favorable Outcome List:", favorable_outcomes)
    print(f"Probability: {probability:.4f}")
    print(f"Percentage: {probability * 100:.2f}%")

twodiceprobabilityanalyzer()