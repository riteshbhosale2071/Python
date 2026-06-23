def difference():
    weight1 = float(input("Enter first weight (kg): "))
    
    weight2 = float(input("Enter second weight (kg): "))

    difference = abs(weight1 - weight2)

    print("Weight Difference =", difference, "kg")

difference()