def missingnumberhcflcm():
    hcf = int(input("Enter the HCF: "))
    lcm = int(input("Enter the LCM: "))
    known_number = int(input("Enter the known number: "))

    if hcf <= 0 or lcm <= 0 or known_number <= 0:
        print("Please enter positive integers.")
        return

    missing_number = (hcf * lcm) // known_number

    if (hcf * lcm) % known_number == 0:
        print("Missing Number:", missing_number)
    else:
        print("No whole-number solution exists.")

missingnumberhcflcm()