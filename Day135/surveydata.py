def surveydata():
    data = list(map(int, input("Enter survey responses separated by spaces: ").split()))

    if not data:
        print("Please enter at least one response.")
        return

    total = sum(data)
    count = len(data)
    average = total / count
    highest = max(data)
    lowest = min(data)

    print("Survey Data Analysis")
    print("Number of Responses:", count)
    print("Total:", total)
    print("Average:", average)
    print("Highest Response:", highest)
    print("Lowest Response:", lowest)
    print("Range:", highest - lowest)

surveydata()