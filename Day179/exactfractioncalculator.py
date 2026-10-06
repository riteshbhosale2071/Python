def exactfractioncalculator():
    print("Exact Fraction Calculator :")

    numerator1 = int(input("Enter first numerator: "))
    denominator1 = int(input("Enter first denominator: "))
    numerator2 = int(input("Enter second numerator: "))
    denominator2 = int(input("Enter second denominator: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
        return

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        numerator = numerator1 * denominator2 + numerator2 * denominator1
        denominator = denominator1 * denominator2

    elif operation == "-":
        numerator = numerator1 * denominator2 - numerator2 * denominator1
        denominator = denominator1 * denominator2

    elif operation == "*":
        numerator = numerator1 * numerator2
        denominator = denominator1 * denominator2

    elif operation == "/":
        if numerator2 == 0:
            print("Cannot divide by zero.")
            return

        numerator = numerator1 * denominator2
        denominator = denominator1 * numerator2

    else:
        print("Invalid operation.")
        return

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    a = abs(numerator)
    b = abs(denominator)

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    gcd = a

    numerator = numerator // gcd
    denominator = denominator // gcd

    print("\nExact Result :")

    if denominator == 1:
        print("Result:", numerator)
    else:
        print("Result:", numerator, "/", denominator)

exactfractioncalculator()