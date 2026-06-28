def monthlyevent():
    n = int(input("Enter number of events: "))

    events = {}

    for i in range(n):
        date = input(f"Enter date for Event {i+1} (DD-MM): ")
        event = input(f"Enter Event {i+1} name: ")
        events[date] = event

    print("\nMonthly Event Tracker")
    print("-" * 35)

    for date in sorted(events):
        print(date, ":", events[date])


monthlyevent()