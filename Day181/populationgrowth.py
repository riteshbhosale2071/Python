def populationgrowth():
    print("Population Growth :")

    population = int(input("Enter initial population: "))
    growth_rate = float(input("Enter annual growth rate (%): "))
    years = int(input("Enter number of years: "))

    if population <= 0 or growth_rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    current_population = population
    total_growth = 0

    print("\nYear\tPopulation\tGrowth")

    for year in range(1, years + 1):
        previous_population = current_population
        current_population = round(current_population * (1 + growth_rate / 100))
        growth = current_population - previous_population
        total_growth += growth

        print(year, "\t", current_population, "\t\t", growth)

    print("\nPopulation Summary :")
    print("Initial Population:", population)
    print("Final Population:", current_population)
    print("Total Population Growth:", total_growth)

    growth_percentage = (total_growth / population) * 100
    print("Overall Growth Percentage:", round(growth_percentage, 2), "%")

populationgrowth()