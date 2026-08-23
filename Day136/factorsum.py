def factorsum():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    factor_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            factor_sum += i

    print("Sum of Factors:", factor_sum)

factorsum()