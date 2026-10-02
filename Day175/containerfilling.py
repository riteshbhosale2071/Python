def containerfilling():
    print("Container Filling Simulator :")

    capacity = float(input("Enter container capacity in liters: "))
    initial_amount = float(input("Enter initial amount of liquid in liters: "))
    filling_rate = float(input("Enter filling rate in liters per minute: "))

    if capacity <= 0 or initial_amount < 0 or filling_rate <= 0:
        print("Enter valid values.")
        return

    if initial_amount > capacity:
        print("Initial amount cannot exceed container capacity.")
        return

    remaining = capacity - initial_amount
    minutes = remaining / filling_rate

    print("\nContainer Capacity:", round(capacity, 2), "liters")
    print("Initial Amount:", round(initial_amount, 2), "liters")
    print("Remaining Capacity:", round(remaining, 2), "liters")
    print("Filling Rate:", round(filling_rate, 2), "liters/minute")
    print("Time Required:", round(minutes, 2), "minutes")

    current_amount = initial_amount
    minute = 0

    print("\nFilling Progress :")

    while current_amount < capacity:
        minute += 1
        current_amount = current_amount + filling_rate

        if current_amount > capacity:
            current_amount = capacity

        print("Minute", minute, ":", round(current_amount, 2), "liters")

    print("\nContainer is completely filled.")

containerfilling()