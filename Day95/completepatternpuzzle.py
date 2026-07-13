def completepattern():
    print("Complete the Pattern:")
    print("2 4 6 8 ?")

    answer = int(input("Enter the missing number: "))

    if answer == 10:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: 10")

completepattern()