def surveysummary():
    participants = int(input("Enter the number of participants: "))

    yes_count = 0

    for i in range(1, participants + 1):
        response = input(f"Participant {i} (Yes/No): ").strip().lower()
        if response == "yes":
            yes_count += 1

    no_count = participants - yes_count

    print("Survey Summary")
    print("Total Participants:", participants)
    print("Yes Responses:", yes_count)
    print("No Responses:", no_count)

surveysummary()