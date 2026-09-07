import math

def exponentialdecay():
    print("Exponential Decay Simulator :")

    initial_value = float(input("Enter initial value: "))
    decay_rate = float(input("Enter decay rate (%): "))
    time = int(input("Enter number of time periods: "))

    if initial_value < 0:
        print("Initial value cannot be negative.")
        return

    if not (0 <= decay_rate <= 100):
        print("Decay rate must be between 0 and 100.")
        return

    if time < 0:
        print("Time cannot be negative.")
        return

    rate = decay_rate / 100
    current_value = initial_value

    print("\nExponential Decay Simulation :")
    print("Initial Value:", initial_value)
    print("Decay Rate:", decay_rate, "%")
    print("Time Periods:", time)

    for period in range(1, time + 1):
        current_value = current_value * (1 - rate)
        print(f"Period {period}: {current_value:.2f}")

    print("\nFinal Value:", round(current_value, 2))
    print("Total Decay:", round(initial_value - current_value, 2))

exponentialdecay()