import random
import math

def linearequationsolver():
    print("\nLinear Equation Solver")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter constant c: "))

    if a == 0:
        print("No unique solution.")
        return

    x = (c - b) / a
    print("Solution: x =", x)


def quadraticequationsolver():
    print("\nQuadratic Equation Solver")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient a cannot be zero.")
        return

    d = b ** 2 - 4 * a * c

    if d > 0:
        print("Root 1:", (-b + math.sqrt(d)) / (2 * a))
        print("Root 2:", (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        print("Repeated Root:", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-d) / abs(2 * a)
        print(f"Root 1: {real} + {imaginary}i")
        print(f"Root 2: {real} - {imaginary}i")


def arithmeticprogressioncalculator():
    print("\nArithmetic Progression Calculator")
    a = float(input("Enter first term: "))
    d = float(input("Enter common difference: "))
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Enter a positive number of terms.")
        return

    last_term = a + (n - 1) * d
    total = n * (a + last_term) / 2

    print("AP Sequence:", [a + i * d for i in range(n)])
    print("Last Term:", last_term)
    print("Sum of Terms:", total)


def financialplanningcalculator():
    print("\nFinancial Planning Calculator")
    income = float(input("Enter monthly income: "))
    expenses = float(input("Enter monthly expenses: "))
    savings = float(input("Enter current savings: "))
    investment = float(input("Enter monthly investment: "))
    annual_rate = float(input("Enter annual investment return (%): "))
    years = int(input("Enter investment period in years: "))

    if min(income, expenses, savings, investment, annual_rate) < 0 or years <= 0:
        print("Invalid financial details.")
        return

    months = years * 12
    rate = annual_rate / 1200

    if rate > 0:
        future_investment = investment * ((1 + rate) ** months - 1) / rate
        future_savings = savings * (1 + rate) ** months
    else:
        future_investment = investment * months
        future_savings = savings

    print("Monthly Balance:", income - expenses)
    print("Monthly Savings Capacity:", max(0, income - expenses))
    print("Total Investment:", investment * months)
    print("Future Investment Value:", round(future_investment, 2))
    print("Future Savings Value:", round(future_savings, 2))
    print("Estimated Total Wealth:", round(future_investment + future_savings, 2))


def probabilitycalculator():
    print("\nProbability Calculator")
    print("1. Coin Toss")
    print("2. Dice Roll")
    print("3. General Event")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        trials = int(input("Enter number of tosses: "))
        if trials <= 0:
            print("Invalid number of tosses.")
            return

        results = [random.choice(["Heads", "Tails"]) for i in range(trials)]
        heads = results.count("Heads")

        print("Results:", results)
        print("Heads Probability:", heads / trials)
        print("Tails Probability:", (trials - heads) / trials)

    elif choice == 2:
        trials = int(input("Enter number of dice rolls: "))
        if trials <= 0:
            print("Invalid number of rolls.")
            return

        target = int(input("Enter target number (1-6): "))
        if target not in range(1, 7):
            print("Invalid dice number.")
            return

        results = [random.randint(1, 6) for i in range(trials)]
        favorable = results.count(target)

        print("Results:", results)
        print("Experimental Probability:", favorable / trials)
        print("Theoretical Probability:", 1 / 6)

    elif choice == 3:
        total = int(input("Enter total possible outcomes: "))
        favorable = int(input("Enter favorable outcomes: "))

        if total <= 0 or favorable < 0 or favorable > total:
            print("Invalid outcome values.")
            return

        print("Probability:", favorable / total)
        print("Percentage:", favorable / total * 100, "%")

    else:
        print("Invalid choice.")


def statisticsanalyzer():
    print("\nStatistics Analyzer")
    n = int(input("Enter number of data values: "))

    if n <= 0:
        print("Enter a positive number of values.")
        return

    data = []

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))
        data.append(value)

    data.sort()

    mean = sum(data) / n

    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    highest_frequency = max(frequency.values())

    if highest_frequency == 1:
        mode = "No Mode"
    else:
        mode = [value for value, count in frequency.items() if count == highest_frequency]

    variance = sum((value - mean) ** 2 for value in data) / n
    standard_deviation = math.sqrt(variance)

    print("Sorted Data:", data)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mode:", mode)
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Range:", max(data) - min(data))
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(standard_deviation, 2))


def mathematicspart1toolkit():
    while True:
        print("\nCOMPLETE MATHEMATICS PART 1 TOOLKIT :")
        print("1. Linear Equations")
        print("2. Quadratic Equations")
        print("3. Arithmetic Progression")
        print("4. Financial Planning")
        print("5. Probability")
        print("6. Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            linearequationsolver()
        elif choice == "2":
            quadraticequationsolver()
        elif choice == "3":
            arithmeticprogressioncalculator()
        elif choice == "4":
            financialplanningcalculator()
        elif choice == "5":
            probabilitycalculator()
        elif choice == "6":
            statisticsanalyzer()
        elif choice == "7":
            print("Thank you for using Mathematics Part 1 Toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")

mathematicspart1toolkit()