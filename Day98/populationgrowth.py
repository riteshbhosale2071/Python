def population_growth(population, growth_rate, years):
    final_population = population * (1 + growth_rate / 100) ** years
    return final_population

population = int(input("Enter current population: "))
growth_rate = float(input("Enter annual growth rate (%): "))
years = int(input("Enter number of years: "))

result = population_growth(population, growth_rate, years)

print("Population after", years, "years =", round(result))