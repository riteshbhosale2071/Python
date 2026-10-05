def mathsquestionclassifier():
    print("Maths Question Classifier :")

    print("1. Basic Arithmetic")
    print("2. Algebra")
    print("3. Geometry")
    print("4. Trigonometry")
    print("5. Calculus")
    print("6. Probability and Statistics")

    topic = int(input("Select question topic: "))
    steps = int(input("Enter number of steps required to solve: "))
    concepts = int(input("Enter number of concepts involved: "))

    if steps <= 0 or concepts <= 0:
        print("Enter valid values.")
        return

    if topic == 1:
        topic_name = "Basic Arithmetic"
    elif topic == 2:
        topic_name = "Algebra"
    elif topic == 3:
        topic_name = "Geometry"
    elif topic == 4:
        topic_name = "Trigonometry"
    elif topic == 5:
        topic_name = "Calculus"
    elif topic == 6:
        topic_name = "Probability and Statistics"
    else:
        print("Invalid topic.")
        return

    difficulty_score = steps + concepts

    if difficulty_score <= 4:
        difficulty = "Easy"
    elif difficulty_score <= 7:
        difficulty = "Medium"
    else:
        difficulty = "Hard"

    print("\nClassification Result :")
    print("Topic:", topic_name)
    print("Number of Steps:", steps)
    print("Number of Concepts:", concepts)
    print("Difficulty Score:", difficulty_score)
    print("Difficulty Level:", difficulty)

mathsquestionclassifier()