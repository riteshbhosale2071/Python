def quadrilateralclassification():
    print("Quadrilateral Classification Quiz")
    print("A quadrilateral has four equal sides and four right angles.")

    answer = input("Enter the quadrilateral type: ").strip().lower()

    correct_answer = "square"

    if answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: Square")

quadrilateralclassification()