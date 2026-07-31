def recipeingredient():
    ingredient = input("Enter the ingredient name: ")
    quantity = float(input("Enter the original quantity: "))
    original_servings = int(input("Enter the original number of servings: "))
    new_servings = int(input("Enter the new number of servings: "))

    new_quantity = (quantity * new_servings) / original_servings

    print("Ingredient:", ingredient)
    print("New Quantity:", new_quantity)

recipeingredient()