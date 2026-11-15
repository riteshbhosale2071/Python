import random

def diceoutcome():
    print("Dice Outcome Simulator")

    rolls = int(input("Enter the number of dice rolls: "))

    if rolls <= 0:
        print("Please enter a positive number of rolls.")
        return

    outcomes = []

    for i in range(rolls):
        result = random.randint(1, 6)
        outcomes.append(result)
        print(f"Roll {i + 1}: {result}")

    print("\nDice Outcome Summary :")
    print("Total Rolls:", rolls)
    print("Total Sum:", sum(outcomes))
    print("Average Outcome:", sum(outcomes) / rolls)

    print("\nFrequency of Each Outcome :")

    for number in range(1, 7):
        count = outcomes.count(number)
        probability = count / rolls
        percentage = probability * 100

        print(f"Number {number}: {count} times ({percentage:.2f}%)")

    most_common = max(range(1, 7), key=outcomes.count)
    print("\nMost Frequent Outcome:", most_common)

diceoutcome()