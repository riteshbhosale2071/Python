def decimaltypeclassifier():
    print("Decimal Type Classifier :")

    value = input("Enter a decimal number: ")

    try:
        number = float(value)
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")
        return

    print("\nClassification Results :")
    print("Entered Value:", value)
    print("Numeric Value:", number)

    if number == int(number):
        print("Classification: Whole-number-valued decimal")
    else:
        print("Classification: Fractional decimal")

    if number > 0:
        print("Sign: Positive")
    elif number < 0:
        print("Sign: Negative")
    else:
        print("Sign: Zero")

    if number == int(number):
        print("Integer Equivalent:", int(number))
    else:
        print("Integer Part:", int(number))
        print("Fractional Part:", abs(number - int(number)))

    if "." in value:
        decimal_part = value.split(".")[-1]
        decimal_part = decimal_part.split("e")[0].split("E")[0]

        if decimal_part.isdigit():
            decimal_places = len(decimal_part)
            print("Decimal Places Entered:", decimal_places)
        else:
            print("Decimal Places: Cannot be determined from the input format.")
    else:
        print("Decimal Places Entered: 0")

    if number == 0:
        print("Final Result: The number is zero.")
    elif number == int(number):
        print("Final Result: The number has no fractional value.")
    else:
        print("Final Result: The number has a fractional value.")

decimaltypeclassifier()