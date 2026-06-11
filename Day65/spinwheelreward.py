import random


def spin():
    rewards = [
        "Chocolate",
        "Toy",
        "Sticker",
        "Book",
        "Pencil",
        "No Reward"
    ]

    reward = random.choice(rewards)

    print("Spinning the Wheel...")
    print("Reward Won:", reward)

spin()