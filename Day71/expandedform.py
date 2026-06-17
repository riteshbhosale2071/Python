def expanded():
    number = input("Enter a number: ")

    length = len(number)
    expanded = []

    for i in range(length):
        digit = int(number[i])

        if digit != 0:
            value = digit * (10 ** (length - i - 1))
            expanded.append(str(value))

    print(" + ".join(expanded))

expanded()