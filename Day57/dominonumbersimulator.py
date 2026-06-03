import random

def domino():

    left = random.randint(0, 6)

    right = random.randint(0, 6)

    print("Domino Tile =", (left, right))

    print("Total =", left + right)

domino()