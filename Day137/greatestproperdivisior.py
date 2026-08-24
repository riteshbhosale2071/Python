def greatestproperdivisor():
    number = int(input("Enter a positive integer: "))

    if number <= 1:
        print("Enter an integer greater than 1.")
        return

    greatest_divisor = 1

    for i in range(1, number):
        if number % i == 0:
            greatest_divisor = i

    print("Greatest Proper Divisor:", greatest_divisor)

greatestproperdivisor()