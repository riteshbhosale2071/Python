def placevalue():
    number = input("Enter an 8-digit number: ")

    if len(number) == 8:
        print("\nPlace Value Chart")
        print("Crore      :", number[0])
        print("Ten Lakh   :", number[1])
        print("Lakh       :", number[2])
        print("Ten Thousand:", number[3])
        print("Thousand   :", number[4])
        print("Hundred    :", number[5])
        print("Ten        :", number[6])
        print("One        :", number[7])
    else:
        print("Please enter an 8-digit number.")

placevalue()