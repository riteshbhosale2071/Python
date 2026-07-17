def divisionestimator():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    estimate = round(dividend / divisor)
    print("Estimated Quotient =", estimate)

divisionestimator()