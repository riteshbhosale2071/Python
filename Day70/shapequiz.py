def shape():
    score = 0

    answer = input("How many sides does a triangle have? ")

    if answer == "3":
        print("Correct")
        score += 1
    else:
        print("Wrong")

    answer = input("How many sides does a square have? ")

    if answer == "4":
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("Final Score =", score)

shape()