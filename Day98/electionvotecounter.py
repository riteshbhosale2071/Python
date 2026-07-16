def vote_counter():
    candidate1 = input("Enter Candidate 1 name: ")
    candidate2 = input("Enter Candidate 2 name: ")

    votes1 = int(input("Enter votes for " + candidate1 + ": "))
    votes2 = int(input("Enter votes for " + candidate2 + ": "))

    if votes1 > votes2:
        print("Winner is", candidate1)
    elif votes2 > votes1:
        print("Winner is", candidate2)
    else:
        print("Election is a Tie")

vote_counter()