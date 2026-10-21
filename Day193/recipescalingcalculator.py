def recipescalingcalculator():
    print("Recipe Scaling Calculator :")

    try:
        n = int(input("Enter the number of ingredients: "))
    except ValueError:
        print("Invalid input! Enter an integer.")
        return

    if n <= 0:
        print("Number of ingredients must be greater than zero.")
        return

    ingredients = []

    for i in range(n):
        print("\nIngredient", i + 1)

        name = input("Enter ingredient name: ")

        try:
            quantity = float(input("Enter original quantity: "))
        except ValueError:
            print("Invalid quantity!")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        unit = input("Enter unit (g, kg, ml, cup, spoon, etc.): ")

        ingredients.append((name, quantity, unit))

    try:
        original_servings = float(input("\nEnter original number of servings: "))
        new_servings = float(input("Enter desired number of servings: "))
    except ValueError:
        print("Invalid serving count!")
        return

    if original_servings <= 0 or new_servings <= 0:
        print("Serving counts must be greater than zero.")
        return

    scaling_factor = new_servings / original_servings

    print("\nRecipe Scaling Results :")
    print("Original Servings:", original_servings)
    print("Desired Servings:", new_servings)
    print("Scaling Factor:", round(scaling_factor, 4))

    print("\nAdjusted Ingredients :")
    print("{:<25} {:<20} {:<15}".format(
        "Ingredient", "Original Quantity", "New Quantity"
    ))
    print("-" * 65)

    for name, quantity, unit in ingredients:
        new_quantity = quantity * scaling_factor

        print("{:<25} {:<20} {:<15}".format(
            name,
            str(quantity) + " " + unit,
            str(round(new_quantity, 4)) + " " + unit
        ))

    print("\nScaling Analysis :")

    if scaling_factor > 1:
        print("The recipe has been increased.")
    elif scaling_factor < 1:
        print("The recipe has been reduced.")
    else:
        print("The recipe quantities remain unchanged.")

    print("Each ingredient quantity was multiplied by the scaling factor.")
    print("Adjust cooking time and seasoning to taste when necessary.")

recipescalingcalculator()