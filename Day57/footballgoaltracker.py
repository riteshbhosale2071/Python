def football():
    team1 = input("Enter Team 1 Name: ")
    team2 = input("Enter Team 2 Name: ")

    goal1 = int(input(f"Goals scored by {team1}: "))
    goal2 = int(input(f"Goals scored by {team2}: "))

    print("\nScoreboard")
    print(team1, ":", goal1)
    print(team2, ":", goal2)

    if goal1 > goal2:
        print(team1, "Wins!")

    elif goal2 > goal1:
        print(team2, "Wins!")

    else:
        print("Match Draw")

football()