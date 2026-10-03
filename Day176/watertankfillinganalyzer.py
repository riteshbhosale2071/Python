def watertankfillinganalyzer():
    print("Water Tank Filling Analyzer :")

    length = float(input("Enter tank length: "))
    width = float(input("Enter tank width: "))
    height = float(input("Enter tank height: "))
    current_level = float(input("Enter current water level: "))
    filling_rate = float(input("Enter filling rate in liters per minute: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("Tank dimensions must be greater than zero.")
        return

    if current_level < 0 or current_level > height:
        print("Current water level must be between 0 and tank height.")
        return

    if filling_rate <= 0:
        print("Filling rate must be greater than zero.")
        return

    tank_volume = length * width * height
    current_volume = length * width * current_level
    remaining_volume = tank_volume - current_volume

    tank_capacity_liters = tank_volume * 1000
    current_water_liters = current_volume * 1000
    remaining_liters = remaining_volume * 1000

    time_required = remaining_liters / filling_rate

    print("\nTank Analysis :")
    print("Tank Capacity:", round(tank_capacity_liters, 2), "liters")
    print("Current Water:", round(current_water_liters, 2), "liters")
    print("Remaining Capacity:", round(remaining_liters, 2), "liters")
    print("Filling Rate:", round(filling_rate, 2), "liters/minute")
    print("Time to Fill:", round(time_required, 2), "minutes")

    if current_level == height:
        print("Tank is already full.")
    elif current_level == 0:
        print("Tank is empty.")
    else:
        percentage = (current_level / height) * 100
        print("Current Fill Percentage:", round(percentage, 2), "%")

watertankfillinganalyzer()