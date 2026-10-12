def tankfillinglevel():
    print("Tank Filling Level :")

    capacity = float(input("Enter total tank capacity in liters: "))
    initial_level = float(input("Enter initial water level in liters: "))
    filling_rate = float(input("Enter water filling rate in liters per minute: "))
    duration = float(input("Enter filling duration in minutes: "))

    if capacity <= 0:
        print("Tank capacity must be greater than zero.")
        return

    if initial_level < 0 or initial_level > capacity:
        print("Initial water level must be between 0 and tank capacity.")
        return

    if filling_rate < 0 or duration < 0:
        print("Filling rate and duration cannot be negative.")
        return

    water_added = filling_rate * duration
    final_level = initial_level + water_added

    if final_level > capacity:
        overflow = final_level - capacity
        final_level = capacity
    else:
        overflow = 0

    remaining_capacity = capacity - final_level
    filling_percentage = (final_level / capacity) * 100

    print("\nTank Filling Report :")
    print("Total Tank Capacity:", round(capacity, 2), "liters")
    print("Initial Water Level:", round(initial_level, 2), "liters")
    print("Water Added:", round(water_added, 2), "liters")
    print("Final Water Level:", round(final_level, 2), "liters")
    print("Remaining Capacity:", round(remaining_capacity, 2), "liters")
    print("Tank Filling Percentage:", round(filling_percentage, 2), "%")
    print("Overflow Amount:", round(overflow, 2), "liters")

    if final_level == capacity:
        print("Tank Status: FULL")
    elif final_level == 0:
        print("Tank Status: EMPTY")
    else:
        print("Tank Status: PARTIALLY FILLED")

tankfillinglevel()