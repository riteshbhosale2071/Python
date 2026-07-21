def decimalnum():
    start = float(input("Enter starting decimal: "))
    end = float(input("Enter ending decimal: "))

    print("Decimal Number Line:")

    number = start
    while number <= end:
        print(round(number, 1))
        number += 0.1

decimalnum()