def sports():
    n = int(input("Enter number of matches: "))

    scores = []

    for i in range(n):
        score = int(input(f"Enter score of Match {i+1}: "))
        scores.append(score)

    print("\nSports Score Report")
    print("-" * 30)

    print("Scores:", scores)
    print("Highest Score =", max(scores))
    print("Lowest Score =", min(scores))
    print("Total Score =", sum(scores))
    print("Average Score =", round(sum(scores) / n, 2))

sports()