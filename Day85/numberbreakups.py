def breakups():
    number = int(input("Enter a number (up to 5 digits): "))

    num = str(number)
    length = len(num)

    print("\nDifferent Breakups of the Number")
    print("-" * 35)

    # Expanded Form
    expanded = []
    for i in range(length):
        digit = int(num[i])
        if digit != 0:
            expanded.append(str(digit * (10 ** (length - i - 1))))
    print("Expanded Form :", " + ".join(expanded))

    # Digit-wise breakup
    print("\nDigit-wise Breakup")
    for i in range(length):
        place = 10 ** (length - i - 1)
        print(num[i], "×", place, "=", int(num[i]) * place)

    # Sum of digits
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    print("\nSum of Digits =", digit_sum)

breakups()