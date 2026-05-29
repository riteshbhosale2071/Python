def count():
    balloons = int(input("Enter total balloons: "))

    burst = 0

    while balloons > 0:

        print("Balloons Left =", balloons)

        pop = int(input("How many balloons burst? "))

        if pop > balloons:
            print("Cannot burst more than available balloons")

        else:
            balloons -= pop
            burst += pop

    print("\nAll balloons burst!")
    print("Total Burst =", burst)

count()