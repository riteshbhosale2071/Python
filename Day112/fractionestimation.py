def fractionestimation():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    guess = float(input("Guess the decimal value: "))

    actual = numerator / denominator

    print("Actual Decimal Value:", actual)

    if abs(actual - guess) <= 0.1:
        print("Good estimation!")
    else:
        print("Try again. Your estimate was not close enough.")

fractionestimation()