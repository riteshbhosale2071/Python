def statisticsquiz():
    print("Statistics Quiz Generator :")

    number_of_values = int(input("Enter the number of values: "))

    if number_of_values <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []

    for i in range(number_of_values):
        value = float(input("Enter value " + str(i + 1) + ": "))
        values.append(value)

    total = 0

    for value in values:
        total += value

    mean = total / number_of_values

    sorted_values = values[:]
    sorted_values.sort()

    if number_of_values % 2 == 1:
        median = sorted_values[number_of_values // 2]
    else:
        middle1 = sorted_values[number_of_values // 2 - 1]
        middle2 = sorted_values[number_of_values // 2]
        median = (middle1 + middle2) / 2

    frequencies = []

    for value in values:
        frequency = 0

        for item in values:
            if item == value:
                frequency += 1

        frequencies.append(frequency)

    highest_frequency = max(frequencies)

    if highest_frequency == 1:
        mode = "No mode"
    else:
        mode = values[frequencies.index(highest_frequency)]

    minimum = min(values)
    maximum = max(values)
    data_range = maximum - minimum

    print("\nStatistics Quiz :")

    score = 0

    print("\nQuestion 1: What is the mean of the dataset?")
    answer1 = float(input("Your answer: "))

    if round(answer1, 2) == round(mean, 2):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(mean, 2))

    print("\nQuestion 2: What is the median of the dataset?")
    answer2 = float(input("Your answer: "))

    if round(answer2, 2) == round(median, 2):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(median, 2))

    print("\nQuestion 3: What is the range of the dataset?")
    answer3 = float(input("Your answer: "))

    if round(answer3, 2) == round(data_range, 2):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", round(data_range, 2))

    print("\nQuestion 4: What is the minimum value?")
    answer4 = float(input("Your answer: "))

    if answer4 == minimum:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", minimum)

    print("\nQuestion 5: What is the maximum value?")
    answer5 = float(input("Your answer: "))

    if answer5 == maximum:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", maximum)

    print("\nQuestion 6: What is the mode of the dataset?")
    answer6 = input("Your answer: ")

    if mode == "No mode":
        if answer6.lower() == "no mode":
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer: No mode")
    else:
        if float(answer6) == mode:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer:", mode)

    print("\nQuiz Result :")
    print("Score:", score, "out of 6")

    if score == 6:
        print("Excellent! All answers are correct.")
    elif score >= 4:
        print("Good performance!")
    elif score >= 2:
        print("Keep practicing.")
    else:
        print("More practice is needed.")

statisticsquiz()