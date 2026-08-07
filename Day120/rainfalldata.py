def rainfalldata():
    days = int(input("Enter number of days: "))

    total_rainfall = 0

    for i in range(1, days + 1):
        rainfall = float(input(f"Enter rainfall for day {i}: "))
        total_rainfall += rainfall

    average = total_rainfall / days

    print("Total Rainfall:", round(total_rainfall, 2), "mm")
    print("Average Rainfall:", round(average, 2), "mm")

rainfalldata()