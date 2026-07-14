def smallestnumber():
    digits = input("Enter 7 digits without spaces: ")

    if len(digits) == 7:
        result = "".join(sorted(digits))
        print("Smallest Number:", result)
    else:
        print("Please enter exactly 7 digits.")

smallestnumber()