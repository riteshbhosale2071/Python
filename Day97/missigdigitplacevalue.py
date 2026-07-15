def missingdigit():
    number = input("Enter a 7-digit number: ")
    position = int(input("Enter missing digit position (1 to 7): "))

    places = [
        "Ten Lakh",
        "Lakh",
        "Ten Thousand",
        "Thousand",
        "Hundred",
        "Ten",
        "One"
    ]

    if len(number) == 7 and 1 <= position <= 7:
        print("Digit:", number[position - 1])
        print("Place Value:", places[position - 1])
    else:
        print("Invalid input.")

missingdigit()