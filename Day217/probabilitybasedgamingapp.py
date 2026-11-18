import random

def probabilitybasedgamingapp():
    print("Probability-Based Gaming Application")

    print("\nSelect a Game:")
    print("1. Coin Toss Game")
    print("2. Dice Rolling Game")
    print("3. Number Guessing Game")
    print("4. Lucky Number Game")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nCoin Toss Game")
        prediction = input("Predict Heads or Tails: ").strip().capitalize()

        if prediction not in ["Heads", "Tails"]:
            print("Invalid prediction.")
            return

        result = random.choice(["Heads", "Tails"])

        print("Actual Result:", result)

        if prediction == result:
            print("Congratulations! You Win.")
        else:
            print("Better Luck Next Time.")

    elif choice == 2:
        print("\nDice Rolling Game")
        prediction = int(input("Predict a number between 1 and 6: "))

        if prediction not in range(1, 7):
            print("Invalid prediction.")
            return

        result = random.randint(1, 6)

        print("Dice Result:", result)

        if prediction == result:
            print("Congratulations! You Win.")
        else:
            print("You Lose.")

    elif choice == 3:
        print("\nNumber Guessing Game")
        secret_number = random.randint(1, 10)
        prediction = int(input("Guess a number between 1 and 10: "))

        if prediction not in range(1, 11):
            print("Invalid prediction.")
            return

        print("Secret Number:", secret_number)

        if prediction == secret_number:
            print("Congratulations! You Win.")
        else:
            print("You Lose.")

    elif choice == 4:
        print("\nLucky Number Game")
        prediction = int(input("Choose a lucky number between 1 and 100: "))

        if prediction not in range(1, 101):
            print("Invalid prediction.")
            return

        result = random.randint(1, 100)

        print("Winning Number:", result)

        if prediction == result:
            print("Jackpot! You Win.")
        else:
            print("Try Again Next Time.")

    else:
        print("Invalid choice.")
        return

    print("\nProbability Analysis:")

    if choice == 1:
        print("Winning Probability: 50%")
    elif choice == 2:
        print("Winning Probability: 16.67%")
    elif choice == 3:
        print("Winning Probability: 10%")
    elif choice == 4:
        print("Winning Probability: 1%")

probabilitybasedgamingapp()