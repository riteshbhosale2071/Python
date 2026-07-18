def primefactor():
    number = int(input("Enter a number: "))

    print("Prime Factors of", number, "are:")

    divisor = 2
    while number > 1:
        while number % divisor == 0:
            print(divisor)
            number = number // divisor
        divisor += 1

primefactor()