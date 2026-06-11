import random

def card():
    cards = ["Ace", "King", "Queen", "Jack"]

    picked = random.choice(cards)

    print("Card Picked:", picked)

card()