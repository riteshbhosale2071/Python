def factorisationchecker():
    number = int(input("Enter the number: "))

    if number == 0:
        print("0 has infinitely many factors.")
        return

    number = abs(number)
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    print("Factors:", factors)

    product = 1
    for factor in factors:
        product *= factor

    print("Factorisation Check:")
    print("Number of Factors:", len(factors))

factorisationchecker()