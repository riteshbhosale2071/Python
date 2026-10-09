def populationdecline():
    print("Population Decline :")

    population = int(input("Enter initial population: "))
    decline_rate = float(input("Enter annual decline rate (%): "))
    years = int(input("Enter number of years: "))

    if population <= 0 or decline_rate < 0 or decline_rate > 100 or years <= 0:
        print("Enter valid values.")
        return

    current_population = population
    total_decline = 0

    print("\nYear\tPopulation\tDecline")

    for year in range(1, years + 1):
        previous_population = current_population
        current_population = round(current_population * (1 - decline_rate / 100))
        decline = previous_population - current_population
        total_decline += decline

        print(year, "\t", current_population, "\t\t", decline)

    print("\nPopulation Decline Summary :")
    print("Initial Population:", population)
    print("Final Population:", current_population)
    print("Total Population Decline:", total_decline)

    decline_percentage = (total_decline / population) * 100
    print("Overall Decline Percentage:", round(decline_percentage, 2), "%")

populationdecline()