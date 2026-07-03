def numbers():
    devanagari = input("Enter a number in Devanagari numerals: ")

    numerals = {
        "०": "0",
        "१": "1",
        "२": "2",
        "३": "3",
        "४": "4",
        "५": "5",
        "६": "6",
        "७": "7",
        "८": "8",
        "९": "9"
    }

    international = ""

    for digit in devanagari:
        if digit in numerals:
            international += numerals[digit]
        else:
            print("Invalid Devanagari numeral.")
            return

    print("\nConversion Result")
    print("-" * 30)
    print("Devanagari Number    :", devanagari)
    print("International Number :", international)

numbers()