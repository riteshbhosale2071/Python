def multiples():
    number = int(input("Enter a number: "))
    multiple = int(input("Enter a multiple of 10: "))

    if multiple % 10 != 0:
        print("Please enter a multiple of 10.")
        return

    product = number * multiple

    print("\nMultiplication Result :")
    print(number, "×", multiple, "=", product)

multiples()