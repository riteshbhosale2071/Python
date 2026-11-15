import random

def cointossprobabilitycalculator():
    print("Coin Toss Probability Calculator")

    tosses = int(input("Enter the number of coin tosses: "))

    if tosses <= 0:
        print("Please enter a positive number of tosses.")
        return

    heads = 0
    tails = 0

    for i in range(tosses):
        result = random.choice(["Heads", "Tails"])

        if result == "Heads":
            heads += 1
        else:
            tails += 1

    heads_probability = heads / tosses
    tails_probability = tails / tosses

    print("\nCoin Toss Results :")
    print("Total Tosses:", tosses)
    print("Heads Count:", heads)
    print("Tails Count:", tails)

    print("\nExperimental Probability :")
    print(f"Probability of Heads: {heads_probability:.4f}")
    print(f"Probability of Tails: {tails_probability:.4f}")

    print("\nPercentage :")
    print(f"Heads Percentage: {heads_probability * 100:.2f}%")
    print(f"Tails Percentage: {tails_probability * 100:.2f}%")

    print("\nTheoretical Probability :")
    print("Probability of Heads: 0.50 (50%)")
    print("Probability of Tails: 0.50 (50%)")

cointossprobabilitycalculator()