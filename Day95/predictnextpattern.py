def predictnext():
    print("Pattern: 5 10 15 20 ?")

    answer = int(input("Enter the next number: "))

    if answer == 25:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: 25")

predictnext()