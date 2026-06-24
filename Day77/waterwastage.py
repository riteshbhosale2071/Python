def wastage():
    flow_rate = float(input("Enter water flow rate (liters/minute): "))
    
    time = float(input("Enter time water was wasted (minutes): "))

    wastage = flow_rate * time

    print("Water Wasted =", wastage, "liters")

wastage()