def fivedigit():
    number = int(input("Enter a five-digit number: "))

    if 10000 <= number <= 99999:
        ten_thousands = number // 10000
        thousands = (number // 1000) % 10
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        digit_sum = ten_thousands + thousands + hundreds + tens + ones

        print("\nFive-Digit Number Report")
        print("-" * 30)
        print("Ten Thousands Digit =", ten_thousands)
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
        print("Please enter a valid five-digit number.")

fivedigit()