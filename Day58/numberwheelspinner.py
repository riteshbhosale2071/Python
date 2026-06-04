import random

def wheel():

    wheel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = random.choice(wheel)

    print("Wheel Stopped At:", result)

wheel()