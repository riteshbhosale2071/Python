def mixtureratiocalculator():
    print("Mixture Ratio Calculator :")

    try:
        n = int(input("Enter the number of ingredients in the mixture: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of ingredients must be greater than zero.")
        return

    ingredients = []

    for i in range(n):
        print("\nIngredient", i + 1)

        name = input("Enter ingredient name: ")

        try:
            quantity = float(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity!")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        ingredients.append((name, quantity))

    total_quantity = sum(quantity for name, quantity in ingredients)

    print("\nMixture Details :")
    print("Total Mixture Quantity:", round(total_quantity, 4))

    if total_quantity == 0:
        print("Cannot calculate ratios because the total quantity is zero.")
        return

    print("\nIndividual Ratios :")

    for name, quantity in ingredients:
        ratio = quantity / total_quantity
        percentage = ratio * 100

        print("Ingredient:", name)
        print("Quantity:", quantity)
        print("Ratio:", round(ratio, 4))
        print("Percentage:", round(percentage, 2), "%")
        print()

    print("Simplified Whole-Number Ratio :")

    if all(quantity.is_integer() for name, quantity in ingredients):
        quantities = [int(quantity) for name, quantity in ingredients]

        gcd = quantities[0]

        for quantity in quantities[1:]:
            a = gcd
            b = quantity

            while b != 0:
                remainder = a % b
                a = b
                b = remainder

            gcd = a

        if gcd > 0:
            simplified = [quantity // gcd for quantity in quantities]
            print("Simplified Ratio:", ":".join(map(str, simplified)))
        else:
            print("All quantities are zero.")
    else:
        print("Quantities include decimals; use the proportions above.")

    print("\nMixture Analysis :")

    largest = max(ingredients, key=lambda item: item[1])
    smallest = min(ingredients, key=lambda item: item[1])

    print("Largest Ingredient:", largest[0], "-", largest[1])
    print("Smallest Ingredient:", smallest[0], "-", smallest[1])
    print("Number of Ingredients:", n)

    if total_quantity > 0:
        print("Mixture calculation completed successfully.")

mixtureratiocalculator()