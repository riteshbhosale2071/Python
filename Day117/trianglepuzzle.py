def trianglepuzzle():
    print("Triangle Puzzle")
    print("A triangle has angles 50° and 60°.")
    
    answer = float(input("Find the third angle: "))

    correct_answer = 70

    if answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")
        print("The correct answer is:", correct_answer, "degrees")

trianglepuzzle()