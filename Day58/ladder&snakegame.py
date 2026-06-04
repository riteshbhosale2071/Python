def game():
    position = 1

    while position < 100:

        dice = int(input("Enter dice value (1-6): "))

        position += dice

        # Ladders
        if position == 4:
            position = 25
            print("🪜 Ladder! Moved to", position)

        elif position == 13:
            position = 46
            print("🪜 Ladder! Moved to", position)

        # Snakes
        elif position == 40:
            position = 10
            print("Snake! Moved to", position)

        elif position == 70:
            position = 35
            print("Snake! Moved to", position)

        print("Current Position =", position)

    print("You Won!")

game()