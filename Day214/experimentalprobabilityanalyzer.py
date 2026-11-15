import random

def experimentalprobabilityanalyzer():
    print("Experimental Probability Analyzer")

    experiments = int(input("Enter the number of experiments: "))

    if experiments <= 0:
        print("Please enter a positive number of experiments.")
        return

    print("\nSelect experiment:")
    print("1. Coin Toss")
    print("2. Dice Roll")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        event = input("Enter event to analyze (Heads/Tails): ").strip().capitalize()

        if event not in ["Heads", "Tails"]:
            print("Invalid event.")
            return

        outcomes = [random.choice(["Heads", "Tails"]) for _ in range(experiments)]
        favorable = outcomes.count(event)
        theoretical_probability = 0.5

    elif choice == 2:
        event = int(input("Enter dice number to analyze (1-6): "))

        if event not in range(1, 7):
            print("Invalid dice number.")
            return

        outcomes = [random.randint(1, 6) for _ in range(experiments)]
        favorable = outcomes.count(event)
        theoretical_probability = 1 / 6

    else:
        print("Invalid choice.")
        return

    experimental_probability = favorable / experiments

    print("\nExperiment Results :")
    print("Total Experiments:", experiments)
    print("All Outcomes:", outcomes)
    print("Favorable Outcomes:", favorable)

    print("\nProbability Analysis :")
    print(f"Experimental Probability: {experimental_probability:.4f}")
    print(f"Theoretical Probability: {theoretical_probability:.4f}")
    print(f"Experimental Percentage: {experimental_probability * 100:.2f}%")
    print(f"Theoretical Percentage: {theoretical_probability * 100:.2f}%")

    difference = abs(experimental_probability - theoretical_probability)
    print(f"Difference: {difference:.4f}")

    if difference < 0.05:
        print("Result: Experimental probability is close to theoretical probability.")
    else:
        print("Result: Experimental probability differs from theoretical probability.")

experimentalprobabilityanalyzer()