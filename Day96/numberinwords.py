def numberinwords():
    words = {
        "0": "Zero", "1": "One", "2": "Two", "3": "Three",
        "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
        "8": "Eight", "9": "Nine"
    }

    number = input("Enter an 8-digit number: ")

    if len(number) == 8:
        print("Number in Words:")
        for digit in number:
            print(words[digit], end=" ")
    else:
        print("Please enter an 8-digit number.")

numberinwords()