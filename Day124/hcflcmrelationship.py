import math

def hcflcmrelationship():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    hcf = math.gcd(a, b)
    lcm = abs(a * b) // hcf

    product_of_numbers = abs(a * b)
    product_of_hcf_lcm = hcf * lcm

    print("HCF:", hcf)
    print("LCM:", lcm)
    print("Product of Numbers:", product_of_numbers)
    print("HCF × LCM:", product_of_hcf_lcm)

    if product_of_numbers == product_of_hcf_lcm:
        print("Relationship Verified!")
    else:
        print("Relationship Not Verified.")

hcflcmrelationship()