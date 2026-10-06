def mathspracticetest():
    print("Maths Practice Test :")

    score = 0
    total_questions = 5

    print("\nQuestion 1:")
    print("What is 25 + 37?")
    print("1. 52")
    print("2. 62")
    print("3. 72")
    print("4. 58")
    answer = int(input("Enter your answer: "))

    if answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is 2.")

    print("\nQuestion 2:")
    print("What is 15 × 6?")
    print("1. 80")
    print("2. 90")
    print("3. 95")
    print("4. 100")
    answer = int(input("Enter your answer: "))

    if answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is 2.")

    print("\nQuestion 3:")
    print("What is the area of a rectangle with length 8 and width 5?")
    print("1. 13")
    print("2. 26")
    print("3. 40")
    print("4. 45")
    answer = int(input("Enter your answer: "))

    if answer == 3:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is 3.")

    print("\nQuestion 4:")
    print("What is 20% of 150?")
    print("1. 20")
    print("2. 25")
    print("3. 30")
    print("4. 35")
    answer = int(input("Enter your answer: "))

    if answer == 3:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is 3.")

    print("\nQuestion 5:")
    print("If x + 12 = 20, what is x?")
    print("1. 6")
    print("2. 8")
    print("3. 10")
    print("4. 12")
    answer = int(input("Enter your answer: "))

    if answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer is 2.")

    percentage = (score / total_questions) * 100

    print("\nTest Result :")
    print("Score:", score, "/", total_questions)
    print("Percentage:", round(percentage, 2), "%")

    if percentage == 100:
        print("Performance: Excellent")
    elif percentage >= 60:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

mathspracticetest()