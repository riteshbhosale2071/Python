def calendar():
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"]

    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    print("\n", months[month - 1], year)
    print("-" * 20)

    for day in range(1, days_in_month[month - 1] + 1):
        print(day)

calendar()