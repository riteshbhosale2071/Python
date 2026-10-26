import random

def automatedstatisticsquiz():
    print("AUTOMATED STATISTICS QUIZ :")

    questions = [
        {
            "question": "1. What is the mean of 2, 4, 6, 8, 10?",
            "options": ["A. 4", "B. 6", "C. 8", "D. 10"],
            "answer": "B",
            "explanation": "Mean = 30 / 5 = 6."
        },
        {
            "question": "2. What is the median of 3, 5, 7, 9, 11?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 9"],
            "answer": "C",
            "explanation": "The middle value of the ordered data is 7."
        },
        {
            "question": "3. What is the mode of 2, 3, 3, 4, 5?",
            "options": ["A. 2", "B. 3", "C. 4", "D. 5"],
            "answer": "B",
            "explanation": "3 occurs more frequently than the other values."
        },
        {
            "question": "4. What is the range of 5, 10, 15, 20?",
            "options": ["A. 5", "B. 10", "C. 15", "D. 20"],
            "answer": "C",
            "explanation": "Range = maximum - minimum = 20 - 5 = 15."
        },
        {
            "question": "5. What is the probability of getting heads on a fair coin toss?",
            "options": ["A. 0", "B. 1/4", "C. 1/2", "D. 1"],
            "answer": "C",
            "explanation": "There is one favorable outcome out of two equally likely outcomes."
        },
        {
            "question": "6. Which measure is most affected by extreme values?",
            "options": ["A. Median", "B. Mean", "C. Mode", "D. Quartile"],
            "answer": "B",
            "explanation": "Extreme values can significantly change the arithmetic mean."
        },
        {
            "question": "7. What is the sum of all relative frequencies in a distribution?",
            "options": ["A. 0", "B. 0.5", "C. 1", "D. 100"],
            "answer": "C",
            "explanation": "Relative frequencies sum to 1, or 100% when expressed as percentages."
        },
        {
            "question": "8. Which graph is commonly used to display a frequency distribution of continuous data?",
            "options": ["A. Histogram", "B. Pie chart", "C. Pictograph", "D. Flowchart"],
            "answer": "A",
            "explanation": "A histogram displays frequencies for continuous data grouped into intervals."
        },
        {
            "question": "9. What is the population variance if every observation is identical?",
            "options": ["A. 0", "B. 1", "C. Equal to the mean", "D. Cannot be determined"],
            "answer": "A",
            "explanation": "Every observation equals the mean, so all squared deviations are zero."
        },
        {
            "question": "10. What does standard deviation measure?",
            "options": ["A. Central value", "B. Data spread", "C. Total frequency", "D. Sample size"],
            "answer": "B",
            "explanation": "Standard deviation measures how spread out values are around the mean."
        }
    ]

    random.shuffle(questions)

    try:
        total_questions = int(input("\nHow many questions do you want (1-10)? "))
    except ValueError:
        print("Invalid input! Enter a whole number.")
        return

    if total_questions < 1 or total_questions > 10:
        print("Please choose between 1 and 10 questions.")
        return

    selected_questions = questions[:total_questions]
    score = 0
    attempted = 0
    wrong_answers = []

    print("\nQuiz started!")
    print("Enter A, B, C, or D to answer each question.")

    for question in selected_questions:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid choice. Enter A, B, C, or D.")
            answer = input("Your answer: ").strip().upper()

        attempted += 1

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])
            wrong_answers.append(question)

        print("Explanation:", question["explanation"])

    percentage = score / attempted * 100

    print("\n" + "=" * 45)
    print("             QUIZ RESULTS")
    print("=" * 45)

    print("Questions Attempted:", attempted)
    print("Correct Answers:", score)
    print("Incorrect Answers:", attempted - score)
    print("Final Score:", str(score) + "/" + str(attempted))
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 90:
        print("Performance: Excellent!")
    elif percentage >= 70:
        print("Performance: Very Good!")
    elif percentage >= 50:
        print("Performance: Good. Keep practicing!")
    else:
        print("Performance: More practice is recommended.")

    if wrong_answers:
        print("\nQuestions to Review :")

        for question in wrong_answers:
            print(question["question"])
            print("Correct Answer:", question["answer"])
            print("Explanation:", question["explanation"])
    else:
        print("\nExcellent! You answered every question correctly.")

    print("\nThank you for participating in the statistics quiz!")

automatedstatisticsquiz()