def decimalplacevalue():
    number = input("Enter a decimal number: ")

    if "." in number:
        whole, decimal = number.split(".")
        places = ["Tenths", "Hundredths", "Thousandths", "Ten Thousandths"]

        for i in range(len(decimal)):
            if i < len(places):
                print(decimal[i], "->", places[i])
    else:
        print("No decimal part found.")

decimalplacevalue()