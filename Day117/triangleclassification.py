def triangleclassification():
    print("Triangle Classification Quiz")
    print("Sides: 5, 5, 5")

    answer = input("Enter the triangle type (Equilateral/Isosceles/Scalene): ").strip().lower()

    correct = "equilateral"

    if answer == correct:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: Equilateral")

triangleclassification()