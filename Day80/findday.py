def findday():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"]

    current_day = input("Enter current day: ").capitalize()
    n = int(input("Enter number of days: "))

    if current_day in days:
        index = days.index(current_day)
        new_index = (index + n) % 7
        print("Day After", n, "Days =", days[new_index])
    else:
        print("Invalid day!")


findday()