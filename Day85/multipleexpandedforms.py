def forms():
    number = input("Enter a number (up to 5 digits): ")

    length = len(number)
    expanded_form = []

    for i in range(length):
        digit = int(number[i])

        if digit != 0:
            place_value = digit * (10 ** (length - i - 1))
            expanded_form.append(str(place_value))

    print("\nExpanded Form")
    print("-" * 30)
    print(number, "=", " + ".join(expanded_form))

forms()