def sportspictograph():
    sport = input("Enter sport name: ")
    score = int(input("Enter score: "))

    print("\nSports Pictograph")
    print(sport + ":", end=" ")

    for i in range(score):
        print("Medal", end=" ")

    print()

sportspictograph()