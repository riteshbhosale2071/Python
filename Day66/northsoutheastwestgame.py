def game():
    direction = input("Enter direction (N/S/E/W): ").upper()

    if direction == "N":
        print("Move North")

    elif direction == "S":
        print("Move South")

    elif direction == "E":
        print("Move East")

    elif direction == "W":
        print("Move West")

    else:
        print("Invalid Direction")

game()