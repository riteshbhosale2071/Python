def holiday():
    holidays = int(input("Enter number of school holidays: "))

    holiday_list = []

    for i in range(holidays):
        holiday = input(f"Enter holiday {i+1}: ")
        holiday_list.append(holiday)

    print("\nSchool Holidays")
    print("-" * 30)

    for holiday in holiday_list:
        print(holiday)

    print("\nTotal School Holidays =", len(holiday_list))


holiday()