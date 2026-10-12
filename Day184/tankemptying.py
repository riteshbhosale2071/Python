def tankemptying():
    print("Tank Emptying :")

    capacity = float(input("Enter total tank capacity in liters: "))
    initial_level = float(input("Enter initial water level in liters: "))
    emptying_rate = float(input("Enter water emptying rate in liters per minute: "))
    duration = float(input("Enter emptying duration in minutes: "))

    if capacity <= 0:
        print("Tank capacity must be greater than zero.")
        return

    if initial_level < 0 or initial_level > capacity:
        print("Initial water level must be between 0 and tank capacity.")
        return

    if emptying_rate < 0 or duration < 0:
        print("Emptying rate and duration cannot be negative.")
        return

    water_removed = emptying_rate * duration
    final_level = initial_level - water_removed

    if final_level < 0:
        excess_emptying = abs(final_level)
        final_level = 0
    else:
        excess_emptying = 0

    remaining_water = final_level
    emptying_percentage = ((initial_level - final_level) / initial_level * 100) if initial_level > 0 else 0

    print("\nTank Emptying Report :")
    print("Total Tank Capacity:", round(capacity, 2), "liters")
    print("Initial Water Level:", round(initial_level, 2), "liters")
    print("Water Removed:", round(water_removed, 2), "liters")
    print("Final Water Level:", round(final_level, 2), "liters")
    print("Remaining Water:", round(remaining_water, 2), "liters")
    print("Emptying Percentage:", round(emptying_percentage, 2), "%")
    print("Excess Emptying Amount:", round(excess_emptying, 2), "liters")

    if final_level == 0:
        print("Tank Status: EMPTY")
    elif final_level == capacity:
        print("Tank Status: FULL")
    else:
        print("Tank Status: PARTIALLY FILLED")

tankemptying()