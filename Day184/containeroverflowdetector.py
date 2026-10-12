def containeroverflowdetector():
    print("Container Overflow Detector :")

    capacity = float(input("Enter container capacity in liters: "))
    current_volume = float(input("Enter current liquid volume in liters: "))
    incoming_rate = float(input("Enter incoming liquid rate in liters per minute: "))
    duration = float(input("Enter filling duration in minutes: "))

    if capacity <= 0:
        print("Container capacity must be greater than zero.")
        return

    if current_volume < 0 or current_volume > capacity:
        print("Current volume must be between zero and container capacity.")
        return

    if incoming_rate < 0 or duration < 0:
        print("Incoming rate and duration cannot be negative.")
        return

    incoming_volume = incoming_rate * duration
    total_volume = current_volume + incoming_volume

    if total_volume > capacity:
        overflow = total_volume - capacity
        final_volume = capacity
        status = "OVERFLOW DETECTED"
    else:
        overflow = 0
        final_volume = total_volume
        status = "NO OVERFLOW"

    remaining_space = capacity - final_volume
    fill_percentage = (final_volume / capacity) * 100

    print("\n=== Container Analysis Report ===")
    print("Container Capacity:", round(capacity, 2), "liters")
    print("Initial Volume:", round(current_volume, 2), "liters")
    print("Incoming Liquid:", round(incoming_volume, 2), "liters")
    print("Final Liquid Volume:", round(final_volume, 2), "liters")
    print("Overflow Amount:", round(overflow, 2), "liters")
    print("Remaining Space:", round(remaining_space, 2), "liters")
    print("Fill Percentage:", round(fill_percentage, 2), "%")
    print("Status:", status)

    if overflow > 0:
        print("Warning: Container capacity will be exceeded.")
    elif remaining_space == 0:
        print("Container is exactly full.")
    else:
        print("Container has enough space for the incoming liquid.")

containeroverflowdetector()