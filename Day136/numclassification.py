def numberclassification():
    number = float(input("Enter a number: "))

    if number == 0:
        print("Classification: Zero")
    elif number > 0:
        print("Classification: Positive")
    else:
        print("Classification: Negative")

    if number.is_integer():
        number = int(number)

        if number % 2 == 0:
            print("Type: Even Integer")
        else:
            print("Type: Odd Integer")
    else:
        print("Type: Decimal Number")

numberclassification()