def sixdigit():
    number = int(input("Enter a six-digit number: "))

    if 100000 <= number <= 999999:
        digits = str(number)

        print("First Digit :", digits[0])
        print("Second Digit:", digits[1])
        print("Third Digit :", digits[2])
        print("Fourth Digit:", digits[3])
        print("Fifth Digit :", digits[4])
        print("Sixth Digit :", digits[5])

        total = sum(int(digit) for digit in digits)
        print("Sum of Digits:", total)
    else:
        print("Please enter a valid six-digit number.")

sixdigit()