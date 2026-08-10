def hcfcalculator():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    def get_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    common_factors = get_factors(abs(numbers[0]))

    for number in numbers[1:]:
        factors = get_factors(abs(number))
        common_factors = [f for f in common_factors if f in factors]

    if common_factors:
        print("Factors of each number:")
        for number in numbers:
            print(number, ":", get_factors(abs(number)))

        print("Common Factors:", common_factors)
        print("HCF:", max(common_factors))
    else:
        print("No common factor found.")

hcfcalculator()