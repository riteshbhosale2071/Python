def multiplegenerator():
    number = int(input("Enter a number: "))
    count = int(input("Enter how many multiples to generate: "))

    print("Multiples of", number, "are:")

    for i in range(1, count + 1):
        print(number * i)

multiplegenerator()