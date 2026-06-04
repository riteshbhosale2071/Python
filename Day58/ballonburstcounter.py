def ballon():
    balloons = int(input("Enter total balloons: "))
    burst = 0

    while balloons > 0:

        pop = int(input("How many balloons burst? "))

        if pop > balloons:
            print("Cannot burst more balloons than available!")

        else:
            balloons -= pop
            burst += pop

            print("Balloons Left =", balloons)

    print("\nAll Balloons Burst!")
    print("Total Balloons Burst =", burst)

ballon()