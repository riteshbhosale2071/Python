def properfactorfinder():
    number = int(input("Enter a positive integer: "))

    if number <= 1:
        print("A number must be greater than 1.")
        return

    factors = []

    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    print("Proper Factors:", factors)

properfactorfinder()