def proportiontablegenerator():
    a = float(input("Enter first value of ratio: "))
    b = float(input("Enter second value of ratio: "))
    terms = int(input("Enter number of rows: "))

    if a <= 0 or b <= 0 or terms <= 0:
        print("Enter positive values.")
        return

    print("\nProportion Table :")
    print("Multiplier\tFirst Value\tSecond Value")

    for i in range(1, terms + 1):
        value1 = a * i
        value2 = b * i

        print(f"{i}\t\t{value1}\t\t{value2}")

proportiontablegenerator()