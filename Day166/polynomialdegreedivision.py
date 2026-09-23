def polynomialdegreedivision():
    print("Polynomial Degree Division Checker :")

    dividend_degree = int(input("Enter the degree of the dividend: "))
    divisor_degree = int(input("Enter the degree of the divisor: "))

    if dividend_degree < 0 or divisor_degree < 0:
        print("Polynomial degrees cannot be negative.")
    elif divisor_degree == 0:
        print("The divisor is a constant polynomial.")
        print("The quotient has the same degree as the dividend.")
    elif dividend_degree < divisor_degree:
        print("The dividend degree is smaller than the divisor degree.")
        print("The quotient is zero and the remainder is the dividend.")
    elif dividend_degree == divisor_degree:
        quotient_degree = 0
        remainder_degree = divisor_degree - 1

        print("The quotient degree is:", quotient_degree)
        print("The remainder degree is at most:", remainder_degree)
    else:
        quotient_degree = dividend_degree - divisor_degree
        remainder_degree = divisor_degree - 1

        print("The quotient degree is:", quotient_degree)
        print("The remainder degree is at most:", remainder_degree)

        if remainder_degree < 0:
            print("The remainder is zero.")
        else:
            print("The remainder degree is at most divisor degree minus one.")

polynomialdegreedivision()