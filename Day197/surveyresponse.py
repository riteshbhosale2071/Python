def surveyresponse():
    print("Survey Response Analyzer :")

    try:
        respondents = int(input("Enter the number of survey respondents: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if respondents <= 0:
        print("Number of respondents must be greater than zero.")
        return

    question = input("Enter the survey question: ")
    responses = []

    print("\nEnter responses for the survey.")
    print("Example: Yes, No, Maybe, Satisfied, Unsatisfied")

    for i in range(respondents):
        response = input(
            "Enter response from respondent " + str(i + 1) + ": "
        ).strip()

        if response == "":
            print("Response cannot be empty.")
            return

        responses.append(response)

    frequency = {}

    for response in responses:
        normalized = response.lower()
        frequency[normalized] = frequency.get(normalized, 0) + 1

    print("\n" + "=" * 45)
    print("          SURVEY ANALYSIS REPORT")
    print("=" * 45)

    print("\nSurvey Question:", question)
    print("Total Respondents:", respondents)
    print("Unique Response Categories:", len(frequency))

    print("\n=== Response Frequency Table ===")
    print("{:<25}{:<12}{:<12}".format(
        "Response", "Count", "Percentage"
    ))
    print("-" * 49)

    for response in sorted(frequency):
        count = frequency[response]
        percentage = count / respondents * 100

        print("{:<25}{:<12}{:<12.2f}".format(
            response, count, percentage
        ))

    print("-" * 49)
    print("{:<25}{:<12}{:<12.2f}".format(
        "Total", respondents, 100.0
    ))

    highest_frequency = max(frequency.values())

    most_common = [
        response for response, count in frequency.items()
        if count == highest_frequency
    ]

    print("\nPopular Responses :")

    if len(most_common) == 1:
        print("Most Common Response:", most_common[0])
        print("Number of Selections:", highest_frequency)
    else:
        print("There is a tie between the following responses:")

        for response in sorted(most_common):
            print(response, "-", frequency[response], "responses")

    print("\nResponse Distribution :")

    for response in sorted(frequency):
        percentage = frequency[response] / respondents * 100
        bar = "*" * int(percentage // 2)

        print(response.capitalize() + ":")
        print(bar, round(percentage, 2), "%")

    print("\nResponse Diversity :")
    diversity_percentage = len(frequency) / respondents * 100

    print("Different Response Categories:", len(frequency))
    print("Category Diversity Percentage:",
          round(diversity_percentage, 2), "%")

    if len(frequency) == 1:
        print("All respondents provided the same response category.")
    elif len(frequency) == respondents:
        print("Every respondent provided a different response category.")
    else:
        print("Responses are distributed across multiple categories.")

    print("\nVerification :")
    total_count = sum(frequency.values())
    total_percentage = sum(
        count / respondents * 100
        for count in frequency.values()
    )

    print("Total Counted Responses:", total_count)
    print("Total Response Percentage:", round(total_percentage, 2), "%")

    if total_count == respondents and abs(total_percentage - 100) < 0.000001:
        print("Verification successful: All responses are accounted for.")
    else:
        print("Verification failed: Check the response data.")

    print("\nSurvey response analysis completed successfully.")

surveyresponse()