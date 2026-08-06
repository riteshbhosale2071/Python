def surveydataorganizer():
    participants = int(input("Enter the number of participants: "))

    total_age = 0

    for i in range(1, participants + 1):
        age = int(input(f"Enter age of participant {i}: "))
        total_age += age

    average_age = total_age / participants

    print("Total Participants:", participants)
    print("Average Age:", round(average_age, 2))

surveydataorganizer()