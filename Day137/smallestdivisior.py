def smallestdivisor():
    number = int(input("Enter a positive integer: "))

    if number <= 1:
        print("Enter an integer greater than 1.")
        return

    for i in range(2, number + 1):
        if number % i == 0:
            print("Smallest Divisor:", i)
            break

smallestdivisor()