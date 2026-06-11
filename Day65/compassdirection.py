def compass():
    direction = input("Enter direction (N/E/S/W): ").upper()

    if direction == "N":
        print("North")

    elif direction == "E":
        print("East")

    elif direction == "S":
        print("South")

    elif direction == "W":
        print("West")

    else:
        print("Invalid Direction")

compass()