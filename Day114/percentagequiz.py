def percentagequiz():
    total = 200
    obtained = 150

    print("Quiz Question:")
    print("If a student scores", obtained, "marks out of", total, "marks,")
    answer = float(input("Enter the percentage: "))

    correct = (obtained / total) * 100

    if round(answer, 2) == round(correct, 2):
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Percentage:", round(correct, 2), "%")

percentagequiz()