def sportsstatistics():
    matches = int(input("Enter number of matches played: "))
    total_runs = int(input("Enter total runs scored: "))

    average = total_runs / matches

    print("Matches Played:", matches)
    print("Total Runs:", total_runs)
    print("Average Runs per Match:", round(average, 2))

sportsstatistics()