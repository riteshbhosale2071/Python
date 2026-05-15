def leap():
    years = (1999, 2000, 2004, 2010, 2024)

    leap = []

    for year in years:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap.append(year)

    print("Leap Years:", tuple(leap))

leap()