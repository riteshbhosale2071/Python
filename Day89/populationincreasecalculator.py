def populationincrease():
    current_population = int(input("Enter current population: "))
    increase = float(input("Enter increase percentage: "))

    new_population = current_population + (current_population * increase / 100)

    print("New Population:", int(new_population))

populationincrease()