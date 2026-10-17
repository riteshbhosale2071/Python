def sportsperformanceanalyzer():
    print("Sports Performance Analyzer :")

    n = int(input("Enter the number of matches played: "))

    if n <= 0:
        print("Number of matches must be greater than zero.")
        return

    scores = []
    wins = 0
    draws = 0
    losses = 0

    for i in range(n):
        print("\nMatch", i + 1)

        score = float(input("Enter points scored: "))
        opponent_score = float(input("Enter opponent's points: "))

        scores.append(score)

        if score > opponent_score:
            wins += 1
        elif score == opponent_score:
            draws += 1
        else:
            losses += 1

    total_points = sum(scores)
    average_points = total_points / n
    highest_score = max(scores)
    lowest_score = min(scores)
    win_percentage = (wins / n) * 100
    draw_percentage = (draws / n) * 100
    loss_percentage = (losses / n) * 100

    print("\nPerformance Summary :")
    print("Matches Played:", n)
    print("Points Scored:", scores)
    print("Total Points:", total_points)
    print("Average Points per Match:", round(average_points, 2))
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)

    print("\nMatch Results :")
    print("Wins:", wins)
    print("Draws:", draws)
    print("Losses:", losses)
    print("Win Percentage:", round(win_percentage, 2), "%")
    print("Draw Percentage:", round(draw_percentage, 2), "%")
    print("Loss Percentage:", round(loss_percentage, 2), "%")

    print("\nPerformance Evaluation :")

    if win_percentage >= 70:
        print("Excellent performance!")
    elif win_percentage >= 50:
        print("Good performance. Keep improving!")
    elif win_percentage >= 30:
        print("Average performance. More practice is needed.")
    else:
        print("Performance needs improvement.")

    if average_points > 0:
        print("The player scored points across the matches.")
    else:
        print("The player did not score any points.")

    if highest_score == lowest_score:
        print("Scoring was consistent across all matches.")
    else:
        print("Scoring varied across the matches.")

sportsperformanceanalyzer()