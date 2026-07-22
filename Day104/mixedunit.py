def mixedunit():
    meters = float(input("Enter length in meters: "))
    kilograms = float(input("Enter weight in kilograms: "))

    centimeters = meters * 100
    grams = kilograms * 1000

    print("Length =", centimeters, "cm")
    print("Weight =", grams, "g")

mixedunit()