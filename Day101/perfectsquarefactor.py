def perfectsquare():
    number = int(input("Enter a number: "))
    i = 1

    while i * i <= number:
        if i * i == number:
            print(number, "is a Perfect Square")
            return
        i += 1

    print(number, "is Not a Perfect Square")

perfectsquare()