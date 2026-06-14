def fuel():
    initial_fuel = float(input("Enter initial fuel (litres): "))
    
    used_fuel = float(input("Enter fuel used (litres): "))

    remaining = initial_fuel - used_fuel

    print("Remaining Fuel =", remaining, "litres")

fuel()