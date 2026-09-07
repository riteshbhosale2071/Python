def exponentialgrowth():
    print("Exponential Growth Simulator :")

    initial_value = float(input("Enter initial value: "))
    growth_rate = float(input("Enter growth rate (%): "))
    time = int(input("Enter number of time periods: "))

    if initial_value < 0:
        print("Initial value cannot be negative.")
        return

    if growth_rate < 0:
        print("Growth rate cannot be negative.")
        return

    if time < 0:
        print("Time cannot be negative.")
        return

    rate = growth_rate / 100

    print("\nExponential Growth Simulation :")
    print("Initial Value:", initial_value)
    print("Growth Rate:", growth_rate, "%")
    print("Time Periods:", time)

    current_value = initial_value

    for period in range(1, time + 1):
        current_value = current_value * (1 + rate)
        print(f"Period {period}: {current_value:.2f}")

    print("\nFinal Value:", round(current_value, 2))
    print("Total Growth:", round(current_value - initial_value, 2))

exponentialgrowth()