def weightedaveragecalculator():
    print("Weighted Average Calculator :")

    try:
        n = int(input("Enter the number of values: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of values must be greater than zero.")
        return

    values = []
    weights = []

    for i in range(n):
        print("\nValue", i + 1)

        try:
            value = float(input("Enter value: "))
            weight = float(input("Enter weight: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if weight < 0:
            print("Weight cannot be negative.")
            return

        values.append(value)
        weights.append(weight)

    total_weight = sum(weights)

    print("\nWeighted Average Table :")
    print("{:<12}{:<15}{:<15}".format(
        "Value", "Weight", "Value * Weight"
    ))
    print("-" * 42)

    weighted_products = []

    for i in range(n):
        product = values[i] * weights[i]
        weighted_products.append(product)

        print("{:<12.2f}{:<15.2f}{:<15.2f}".format(
            values[i], weights[i], product
        ))

    total_product = sum(weighted_products)

    print("-" * 42)
    print("Sum of Weights:", round(total_weight, 2))
    print("Sum of Weighted Products:", round(total_product, 2))

    if total_weight == 0:
        print("\nWeighted average cannot be calculated because total weight is zero.")
        return

    weighted_average = total_product / total_weight

    print("\nWeighted Average Result :")
    print("Formula: Weighted Average = Sum(value * weight) / Sum(weights)")
    print("Weighted Average:", round(weighted_average, 4))

    print("\nWeight Percentages :")

    for i in range(n):
        percentage = (weights[i] / total_weight) * 100

        print(
            "Value:", values[i],
            "| Weight:", weights[i],
            "| Weight Percentage:", round(percentage, 2), "%"
        )

    print("\nVerification :")
    print("Total Weight:", round(total_weight, 2))
    print("Total Weighted Product:", round(total_product, 2))

    if abs(sum(weighted_products) - total_product) < 0.000001:
        print("Verification successful: All weighted products are included.")
    else:
        print("Verification failed: Please check the calculations.")

    print("\nSummary :")
    print("Number of Values:", n)
    print("Minimum Value:", min(values))
    print("Maximum Value:", max(values))
    print("Weighted Average:", round(weighted_average, 4))

weightedaveragecalculator()