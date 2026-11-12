def appositionfinder():
    try:
        first_term = float(input("Enter first term (a): "))
        common_difference = float(input("Enter common difference (d): "))
        target_term = float(input("Enter the term to find: "))

        if common_difference == 0:
            if target_term == first_term:
                print("The term occurs at every position.")
            else:
                print("The term is not present in the AP.")
            return

        position = (target_term - first_term) / common_difference + 1

        if position > 0 and position.is_integer():
            print("Term Found!")
            print("Position of the term:", int(position))
        else:
            print("The given term is not present in the AP.")

    except ValueError:
        print("Please enter valid numeric values.")

appositionfinder()