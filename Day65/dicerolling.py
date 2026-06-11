import random

def dice():
    player1 = random.randint(1, 6)
    player2 = random.randint(1, 6)

    print("Player 1 rolled:", player1)
    print("Player 2 rolled:", player2)

    if player1 > player2:
        print("Player 1 Wins!")

    elif player2 > player1:
        print("Player 2 Wins!")

    else:
        print("It's a Tie!")

dice()