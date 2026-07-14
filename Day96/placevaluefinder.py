def valuefinder():
    number = input("Enter an 8-digit number: ")

    if len(number) == 8:
        place = input("Enter place (Crore, Ten Lakh, Lakh, Ten Thousand, Thousand, Hundred, Ten, One): ")

        if place == "Crore":
            print("Place Value:", int(number[0]) * 10000000)
        elif place == "Ten Lakh":
            print("Place Value:", int(number[1]) * 1000000)
        elif place == "Lakh":
            print("Place Value:", int(number[2]) * 100000)
        elif place == "Ten Thousand":
            print("Place Value:", int(number[3]) * 10000)
        elif place == "Thousand":
            print("Place Value:", int(number[4]) * 1000)
        elif place == "Hundred":
            print("Place Value:", int(number[5]) * 100)
        elif place == "Ten":
            print("Place Value:", int(number[6]) * 10)
        elif place == "One":
            print("Place Value:", int(number[7]))
        else:
            print("Invalid place.")
    else:
        print("Please enter an 8-digit number.")

valuefinder()