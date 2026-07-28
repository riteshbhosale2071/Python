def temperatureinteger():
    temperature = int(input("Enter the temperature: "))

    if temperature > 0:
        print("Above Freezing")
    elif temperature < 0:
        print("Below Freezing")
    else:
        print("Freezing Point")

temperatureinteger()