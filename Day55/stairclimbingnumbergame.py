def stair():
    stairs = int(input("Enter total stairs: "))
    step = int(input("Enter steps climbed each time: "))

    position = 0

    while position < stairs:

        position += step

        if position > stairs:
            position = stairs

        print("Reached Stair", position)

    print("You reached the top!")

stair()