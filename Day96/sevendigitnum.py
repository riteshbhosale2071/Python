def sevendigit():
    number = int(input("Enter a seven-digit number: "))

    if 1000000 <= number <= 9999999:
        digits = str(number)

        print("First Digit :", digits[0])
        print("Second Digit:", digits[1])
        print("Third Digit :", digits[2])
        print("Fourth Digit:", digits[3])
        print("Fifth Digit :", digits[4])
        print("Sixth Digit :", digits[5])
        print("Seventh Digit:", digits[6])

        total = sum(int(digit) for digit in digits)
        print("Sum of Digits:", total)
    else:
        print("Please enter a valid seven-digit number.")

sevendigit()