def measurementpractice():
    length1 = 15
    length2 = 8

    print("Find the total length.")
    print("Length 1 =", length1, "cm")
    print("Length 2 =", length2, "cm")

    answer = float(input("Enter your answer (cm): "))

    correct = length1 + length2

    if answer == correct:
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", correct, "cm")

measurementpractice()