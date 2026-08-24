def abundantnumberchecker():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return

    factor_sum = 0

    for i in range(1, number):
        if number % i == 0:
            factor_sum += i

    if factor_sum > number:
        print("The number is an Abundant Number.")
    else:
        print("The number is not an Abundant Number.")

abundantnumberchecker()