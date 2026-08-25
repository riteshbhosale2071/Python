def repeatingevent():
    intervals = list(map(int, input(
        "Enter event intervals in minutes separated by spaces: "
    ).split()))

    if not intervals or any(interval <= 0 for interval in intervals):
        print("Please enter positive intervals.")
        return

    simulation_time = int(input("Enter simulation time in minutes: "))

    if simulation_time < 0:
        print("Simulation time cannot be negative.")
        return

    print("\nRepeating Event Schedule:")

    for i, interval in enumerate(intervals, start=1):
        events = list(range(0, simulation_time + 1, interval))
        print(f"Event {i} (every {interval} min): {events}")

repeatingevent()