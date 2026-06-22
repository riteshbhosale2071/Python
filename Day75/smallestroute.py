def smallest():
    route1 = float(input("Enter route1 in kms:"))
    route2 = float(input("Enter route2 in kms:"))
    route3 = float(input("Enter route3 in kms:"))

    smallest = min(route1,route2,route3)

    print("Smallest route is",smallest)

smallest()