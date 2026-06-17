def converter():
    numbers = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }

    num = int(input("Enter a number (0-10): "))

    print(numbers.get(num, "Number not available"))

converter()