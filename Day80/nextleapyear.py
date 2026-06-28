def leapyear():
    year = int(input("Enter a year: "))

    while True:
        year += 1

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("Next Leap Year =", year)
            break


leapyear()