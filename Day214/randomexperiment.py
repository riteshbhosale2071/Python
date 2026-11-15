import random

def randomexperiment():
    print("Random Experiment Simulator")
    print("1. Coin Toss")
    print("2. Dice Roll")
    print("3. Random Number Generator")
    print("4. Multiple Coin Tosses")
    print("5. Multiple Dice Rolls")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = random.choice(["Heads", "Tails"])
        print("Coin Toss Result:", result)

    elif choice == 2:
        result = random.randint(1, 6)
        print("Dice Roll Result:", result)

    elif choice == 3:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range.")
        else:
            print("Random Number:", random.randint(start, end))

    elif choice == 4:
        times = int(input("Enter number of tosses: "))

        if times <= 0:
            print("Enter a positive number.")
            return

        heads = 0
        tails = 0

        for i in range(times):
            result = random.choice(["Heads", "Tails"])
            print(f"Toss {i + 1}: {result}")

            if result == "Heads":
                heads += 1
            else:
                tails += 1

        print("\nHeads:", heads)
        print("Tails:", tails)
        print("Heads Percentage:", heads / times * 100, "%")
        print("Tails Percentage:", tails / times * 100, "%")

    elif choice == 5:
        times = int(input("Enter number of dice rolls: "))

        if times <= 0:
            print("Enter a positive number.")
            return

        results = []

        for i in range(times):
            result = random.randint(1, 6)
            results.append(result)
            print(f"Roll {i + 1}: {result}")

        print("\nTotal:", sum(results))
        print("Average:", sum(results) / times)

        for number in range(1, 7):
            print(f"Number {number} appeared {results.count(number)} times")

    else:
        print("Invalid choice.")

randomexperiment()