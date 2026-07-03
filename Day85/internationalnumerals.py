def numerals():
    number = int(input("Enter a number (up to 5 digits): "))

    if 0 <= number <= 99999:
        ten_thousands = number // 10000
        thousands = (number // 1000) % 10
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        print("\nInternational Place Value")
        print("-" * 40)
        print("Ten-Thousands :", ten_thousands)
        print("Thousands     :", thousands)
        print("Hundreds      :", hundreds)
        print("Tens          :", tens)
        print("Ones          :", ones)
    else:
        print("Please enter a number up to 5 digits.")

numerals()