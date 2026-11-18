def surveydataanalysis():
    print("Survey Data Analysis :")

    n = int(input("Enter the number of survey participants: "))

    if n <= 0:
        print("Please enter a positive number of participants.")
        return

    responses = []

    for i in range(n):
        print(f"\nParticipant {i + 1}")
        response = input("Enter survey response: ").strip()

        if not response:
            print("Response cannot be empty.")
            return

        responses.append(response)

    frequency = {}

    for response in responses:
        frequency[response] = frequency.get(response, 0) + 1

    print("\nSurvey Frequency Table:")
    print(f"{'Response':<20}{'Frequency':<15}{'Percentage':<15}")

    for response, count in sorted(frequency.items()):
        percentage = (count / n) * 100
        print(f"{response:<20}{count:<15}{percentage:.2f}%")

    highest_frequency = max(frequency.values())

    popular_responses = [
        response for response, count in frequency.items()
        if count == highest_frequency
    ]

    print("\nSurvey Analysis:")
    print("Total Participants:", n)
    print("Unique Responses:", len(frequency))
    print("Most Common Response:", popular_responses)
    print("Highest Frequency:", highest_frequency)
    print("Response Diversity:", round(len(frequency) / n * 100, 2), "%")

    print("\nAll Responses:")
    for i, response in enumerate(responses, start=1):
        print(f"Participant {i}: {response}")

surveydataanalysis()