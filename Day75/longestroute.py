def longest():
    route1 = float(input("Enter route1 in kms: "))
    route2 = float(input("Enter route2 in kms: "))
    route3 = float(input("Enter route3 in kms: "))

    longest = max(route1,route2,route3)

    print("Longest root is",longest)

longest()