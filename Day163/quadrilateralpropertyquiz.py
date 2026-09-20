def quadrilateralpropertyquiz():
    print("Quadrilateral Property Quiz :")

    score = 0

    print("\nQuestion 1: How many sides does a quadrilateral have?")
    print("1. 3")
    print("2. 4")
    print("3. 5")
    answer = input("Enter your answer: ")

    if answer == "2":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nQuestion 2: What is the sum of the interior angles of a quadrilateral?")
    print("1. 180 degrees")
    print("2. 270 degrees")
    print("3. 360 degrees")
    answer = input("Enter your answer: ")

    if answer == "3":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nQuestion 3: Which quadrilateral has four equal sides?")
    print("1. Rectangle")
    print("2. Rhombus")
    print("3. Trapezium")
    answer = input("Enter your answer: ")

    if answer == "2":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nQuestion 4: Which quadrilateral has four right angles?")
    print("1. Rectangle")
    print("2. Kite")
    print("3. Rhombus")
    answer = input("Enter your answer: ")

    if answer == "1":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nQuestion 5: Which quadrilateral has two pairs of parallel sides?")
    print("1. Parallelogram")
    print("2. Kite")
    print("3. Trapezium")
    answer = input("Enter your answer: ")

    if answer == "1":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("\nYour final score is:", score, "out of 5")

    if score == 5:
        print("Excellent performance!")
    elif score >= 3:
        print("Good performance!")
    else:
        print("Keep practicing!")

quadrilateralpropertyquiz()