def fourdigit():
    number = int(input("Enter a four-digit number: "))

    if 1000 <= number <= 9999:
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        digit_sum = thousands + hundreds + tens + ones

        print("\nFour-Digit Number Report")
        print("-" * 30)
        print("Thousands Digit =", thousands)
        print("Hundreds Digit =", hundreds)
        print("Tens Digit =", tens)
        print("Ones Digit =", ones)
        print("Sum of Digits =", digit_sum)

        if number % 2 == 0:
            print("Number is Even")
        else:
            print("Number is Odd")
    else:
        print("Please enter a valid four-digit number.")

fourdigit()