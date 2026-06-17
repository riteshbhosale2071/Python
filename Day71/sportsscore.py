def sports():
    scores = []

    n = int(input("Enter number of matches: "))

    for i in range(n):
        score = int(input(f"Enter score for match {i+1}: "))
        scores.append(score)

    print("Highest Score =", max(scores))
    print("Lowest Score =", min(scores))
    print("Average Score =", sum(scores) / len(scores))

sports()