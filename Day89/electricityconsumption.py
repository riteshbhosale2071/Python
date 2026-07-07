def electricitybill():
    previous = int(input("Enter previous meter reading: "))
    current = int(input("Enter current meter reading: "))
    rate = float(input("Enter cost per unit: "))

    units = current - previous
    bill = units * rate

    print("Units Consumed:", units)
    print("Electricity Bill:", bill)

electricitybill()