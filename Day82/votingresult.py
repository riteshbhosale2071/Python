def voting():
    n = int(input("Enter number of voters: "))

    votes = {}

    for i in range(n):
        candidate = input(f"Enter vote {i+1}: ").capitalize()

        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

    print("\nVoting Results")
    print("-" * 30)

    for candidate, count in votes.items():
        print(candidate, ":", count)

    winner = max(votes, key=votes.get)

    print("\nWinner =", winner)
    print("Total Votes =", votes[winner])

voting()