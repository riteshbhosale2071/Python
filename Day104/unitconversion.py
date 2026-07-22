def unitconverter():
    meters = float(input("Enter length in meters: "))

    centimeters = meters * 100
    kilometers = meters / 1000

    print("Centimeters =", centimeters)
    print("Kilometers =", kilometers)

unitconverter()