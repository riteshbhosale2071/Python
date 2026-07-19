def multiplequiz():
    number = int(input("Enter a number: "))
    answer = int(input("What is the 5th multiple of " + str(number) + "? "))

    if answer == number * 5:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer =", number * 5)

multiplequiz()