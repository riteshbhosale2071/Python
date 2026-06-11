import random

def coin():
    n = int(input("How many tosses? "))

    heads = 0
    tails = 0

    for i in range(n):

        toss = random.choice(["Heads", "Tails"])

        if toss == "Heads":
            heads += 1
        else:
            tails += 1

    print("Heads =", heads)
    print("Tails =", tails)

coin()