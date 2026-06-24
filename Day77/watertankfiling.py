def tank():
    tank_capacity = float(input("Enter tank capacity (liters): "))
    
    fill_rate = float(input("Enter filling rate (liters/minute): "))

    time_required = tank_capacity / fill_rate

    print("Time Required =", round(time_required, 2), "minutes")

tank()