def abacus():
    number = input("Enter a 5-digit number: ")

    if len(number) == 5 and number.isdigit():

        places = ["Ten-Thousands", "Thousands", "Hundreds", "Tens", "Ones"]

        print("\nNumber Abacus")
        print("-" * 35)

        for i in range(5):
            print(places[i], ":", "●" * int(number[i]), f"({number[i]})")
    else:
        print("Please enter a valid 5-digit number.")

abacus()