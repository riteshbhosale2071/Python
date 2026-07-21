def measurementconverter():
    meters = float(input("Enter measurement in meters: "))
    centimeters = meters * 100
    kilometers = meters / 1000

    print("Centimeters =", centimeters)
    print("Kilometers =", kilometers)

measurementconverter()