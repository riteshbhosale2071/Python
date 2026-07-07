def divisionquiz():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    answer = int(input("Enter the quotient: "))

    correct = dividend // divisor

    if answer == correct:
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
        print("Correct Quotient:", correct)

divisionquiz()