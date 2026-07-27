def anglepuzzle():
    angle1 = 45
    angle2 = 45

    print("Puzzle:")
    print("Angle 1 =", angle1)
    print("Angle 2 =", angle2)
    answer = int(input("What is the total angle? "))

    if answer == angle1 + angle2:
        print("Correct!")
    else:
        print("Wrong! The correct answer is", angle1 + angle2)

anglepuzzle()