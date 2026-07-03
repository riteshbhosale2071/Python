def chart():
    number = int(input("Enter a number (up to 5 digits): "))

    if 0 <= number <= 99999:
        number = str(number).zfill(5)

        print("\nPlace Value Chart")
        print("-" * 60)
        print("Ten-Thousands\tThousands\tHundreds\tTens\tOnes")
        print(number[0], "\t\t", number[1], "\t\t", number[2], "\t\t", number[3], "\t", number[4])
    else:
        print("Please enter a number up to 5 digits.")

chart()