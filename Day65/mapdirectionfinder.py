def map():
    direction = input("Enter direction (N/S/E/W): ").upper()

    if direction == "N":
        print("North")

    elif direction == "S":
        print("South")

    elif direction == "E":
        print("East")

    elif direction == "W":
        print("West")

    else:
        print("Invalid Direction")

map()