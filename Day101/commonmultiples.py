def commonmultiples():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    count = int(input("Enter how many common multiples: "))

    found = 0
    multiple = 1

    print("Common Multiples are:")

    while found < count:
        if multiple % num1 == 0 and multiple % num2 == 0:
            print(multiple)
            found += 1
        multiple += 1

commonmultiples()