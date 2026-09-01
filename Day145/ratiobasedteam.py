def ratiobasedteam():
    total_members = int(input("Enter total number of members: "))
    ratio1 = int(input("Enter ratio for Team 1: "))
    ratio2 = int(input("Enter ratio for Team 2: "))

    if total_members <= 0 or ratio1 <= 0 or ratio2 <= 0:
        print("Enter positive values.")
        return

    total_ratio = ratio1 + ratio2

    if total_members % total_ratio != 0:
        print("Teams cannot be formed exactly according to the given ratio.")
        return

    team1 = (total_members * ratio1) // total_ratio
    team2 = (total_members * ratio2) // total_ratio

    print("\nTeam Formation :")
    print("Team 1 Members:", team1)
    print("Team 2 Members:", team2)
    print("Total Members:", team1 + team2)

ratiobasedteam()