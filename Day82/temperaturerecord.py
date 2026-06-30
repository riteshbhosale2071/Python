def temperature():
    n = int(input("Enter number of temperature records: "))

    temperatures = []

    for i in range(n):
        temp = float(input(f"Enter temperature {i+1} (°C): "))
        temperatures.append(temp)

    print("\nTemperature Report")
    print("-" * 30)

    print("Temperature Records:", temperatures)
    print("Highest Temperature =", max(temperatures), "°C")
    print("Lowest Temperature =", min(temperatures), "°C")
    print("Average Temperature =", round(sum(temperatures) / n, 2), "°C")

temperature()