def constructionquiz():
    print("Construction Quiz")
    print("Which tool is mainly used to draw a circle?")
    print("1. Ruler")
    print("2. Compass")
    print("3. Protractor")
    print("4. Set Square")

    answer = int(input("Enter your answer (1-4): "))

    if answer == 2:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: Compass")

constructionquiz()