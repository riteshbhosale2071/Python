def rearrangement():
    number = input("Enter a 5-digit number: ")

    if len(number) != 5 or not number.isdigit():
        print("Please enter a valid 5-digit number.")
        return

    digits = list(number)

    ascending = sorted(digits)
    descending = sorted(digits, reverse=True)

    smallest = ""
    largest = ""

    if ascending[0] == "0":
        for i in range(1, len(ascending)):
            if ascending[i] != "0":
                ascending[0], ascending[i] = ascending[i], ascending[0]
                break

    for digit in ascending:
        smallest += digit

    for digit in descending:
        largest += digit

    difference = int(largest) - int(smallest)

    print("\nDigit Rearrangement Report")
    print("-" * 35)
    print("Original Number :", number)
    print("Largest Number  :", largest)
    print("Smallest Number :", smallest)
    print("Difference      :", difference)

rearrangement()