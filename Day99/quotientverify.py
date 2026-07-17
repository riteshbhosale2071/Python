def verifyquotient():
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    user_quotient = int(input("Enter quotient: "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    correct_quotient = dividend // divisor

    if user_quotient == correct_quotient:
        print("Correct! Quotient Verified.")
    else:
        print("Incorrect!")
        print("Correct Quotient =", correct_quotient)

verifyquotient()