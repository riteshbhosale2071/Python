def patternquiz():
    print("Find the missing number:")
    print("3 6 9 ? 15")

    answer = int(input("Enter your answer: "))

    if answer == 12:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: 12")

patternquiz()