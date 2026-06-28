def reminder():
    n = int(input("Enter number of festivals: "))

    festivals = {}

    for i in range(n):
        date = input(f"Enter date for Festival {i+1} (DD-MM): ")
        festival = input(f"Enter Festival {i+1} name: ")
        festivals[date] = festival

    today = input("\nEnter today's date (DD-MM): ")

    if today in festivals:
        print("Reminder:", festivals[today], "is today!")
    else:
        print("No festival today.")

    print("\nFestival List")
    print("-" * 30)

    for date in sorted(festivals):
        print(date, ":", festivals[date])


reminder()