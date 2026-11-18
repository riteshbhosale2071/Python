import random

def probabilityexperiment():
    print("Probability Experiment Analyzer")

    print("\nSelect an Experiment:")
    print("1. Coin Toss")
    print("2. Dice Roll")
    print("3. Two Dice Roll")
    print("4. Random Number Experiment")

    choice = int(input("Enter your choice: "))
    trials = int(input("Enter number of trials: "))

    if trials <= 0:
        print("Please enter a positive number of trials.")
        return

    outcomes = []
    favorable = 0

    if choice == 1:
        event = input("Enter event (Heads/Tails): ").strip().capitalize()

        if event not in ["Heads", "Tails"]:
            print("Invalid event.")
            return

        for i in range(trials):
            result = random.choice(["Heads", "Tails"])
            outcomes.append(result)

            if result == event:
                favorable += 1

        theoretical_probability = 0.5

    elif choice == 2:
        event = int(input("Enter dice number (1-6): "))

        if event not in range(1, 7):
            print("Invalid dice number.")
            return

        for i in range(trials):
            result = random.randint(1, 6)
            outcomes.append(result)

            if result == event:
                favorable += 1

        theoretical_probability = 1 / 6

    elif choice == 3:
        event = int(input("Enter target sum (2-12): "))

        if event not in range(2, 13):
            print("Invalid target sum.")
            return

        for i in range(trials):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            result = die1 + die2
            outcomes.append((die1, die2))

            if result == event:
                favorable += 1

        theoretical_probability = sum(
            1 for i in range(1, 7)
            for j in range(1, 7)
            if i + j == event
        ) / 36

    elif choice == 4:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range.")
            return

        event = int(input("Enter target number: "))

        if event < start or event > end:
            print("Target number is outside the range.")
            return

        for i in range(trials):
            result = random.randint(start, end)
            outcomes.append(result)

            if result == event:
                favorable += 1

        theoretical_probability = 1 / (end - start + 1)

    else:
        print("Invalid choice.")
        return

    experimental_probability = favorable / trials

    print("\nProbability Experiment Results:")
    print("Total Trials:", trials)
    print("Outcomes:", outcomes)
    print("Favorable Outcomes:", favorable)
    print("Unfavorable Outcomes:", trials - favorable)

    print("\nProbability Analysis:")
    print("Experimental Probability:", round(experimental_probability, 4))
    print("Theoretical Probability:", round(theoretical_probability, 4))
    print("Experimental Percentage:", round(experimental_probability * 100, 2), "%")
    print("Theoretical Percentage:", round(theoretical_probability * 100, 2), "%")
    print("Probability Difference:", round(abs(experimental_probability - theoretical_probability), 4))

probabilityexperiment()