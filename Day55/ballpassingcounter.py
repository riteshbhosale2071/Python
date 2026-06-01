def counter():
    players = int(input("Enter number of players: "))
    passes = int(input("Enter number of passes: "))

    current = 1

    for i in range(passes):

        current = (current % players) + 1

    print("Ball is with Player", current)

counter()