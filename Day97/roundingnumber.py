def numberrounding():
    number = int(input("Enter a number: "))
    nearest = int(input("Round to nearest (10, 100, 1000): "))

    rounded = round(number / nearest) * nearest

    print("Rounded Number:", rounded)

numberrounding()