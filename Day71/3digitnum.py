def threedigit():
    digits = input("Enter three digits separated by space: ").split()

    digits.sort(reverse=True)

    greatest = "".join(digits)

    print("Greatest 3-Digit Number =", greatest)

threedigit()