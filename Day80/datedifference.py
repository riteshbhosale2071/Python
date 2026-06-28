def date():
    day1 = int(input("Enter first date (day): "))
    month1 = int(input("Enter first month: "))
    year1 = int(input("Enter first year: "))

    day2 = int(input("\nEnter second date (day): "))
    month2 = int(input("Enter second month: "))
    year2 = int(input("Enter second year: "))

    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    total_days1 = year1 * 365 + sum(days_in_month[:month1 - 1]) + day1
    total_days2 = year2 * 365 + sum(days_in_month[:month2 - 1]) + day2

    difference = abs(total_days2 - total_days1)

    print("\nDifference Between Dates =", difference, "days")


date()