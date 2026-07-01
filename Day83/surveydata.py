def data():
    n = int(input("Enter number of participants: "))

    responses = {}

    for i in range(n):
        answer = input(f"Enter response of participant {i+1}: ").capitalize()

        if answer in responses:
            responses[answer] += 1
        else:
            responses[answer] = 1

    print("\nSurvey Report")
    print("-" * 30)

    total = 0

    for answer, count in responses.items():
        print(answer, ":", count)
        total += count

    print("\nTotal Participants =", total)

data()