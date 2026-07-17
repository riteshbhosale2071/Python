def scientificgrant():
    researchers = int(input("Enter number of researchers: "))
    grant_per_researcher = float(input("Enter grant amount per researcher: "))

    total_grant = researchers * grant_per_researcher

    print("Total Scientific Grant =", total_grant)

scientificgrant()