def electionresult():
    candidate1 = int(input("Enter votes for Candidate 1: "))
    candidate2 = int(input("Enter votes for Candidate 2: "))

    print("Candidate 1 Votes:", candidate1)
    print("Candidate 2 Votes:", candidate2)

    if candidate1 > candidate2:
        print("Winner: Candidate 1")
    elif candidate2 > candidate1:
        print("Winner: Candidate 2")
    else:
        print("Result: Tie")

electionresult()