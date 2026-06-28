def birthdaycountdown():
    current_day = int(input("Enter current day: "))
    current_month = int(input("Enter current month: "))

    birthday_day = int(input("Enter birthday day: "))
    birthday_month = int(input("Enter birthday month: "))

    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    current_days = current_day
    for i in range(current_month - 1):
        current_days += days_in_month[i]

    birthday_days = birthday_day
    for i in range(birthday_month - 1):
        birthday_days += days_in_month[i]

    if birthday_days >= current_days:
        remaining_days = birthday_days - current_days
    else:
        remaining_days = 365 - current_days + birthday_days

    print("Days Remaining Until Birthday =", remaining_days)


birthdaycountdown()