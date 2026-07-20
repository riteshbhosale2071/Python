def decimalreader():
    number = input("Enter a decimal number: ")
    print("Digits are:")

    for digit in number:
        if digit == ".":
            print("Point")
        else:
            print(digit)

decimalreader()