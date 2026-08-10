import math

def coprimepair():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd = math.gcd(num1, num2)

    if gcd == 1:
        print("The numbers are Co-Prime.")
    else:
        print("The numbers are not Co-Prime.")
        print("GCD:", gcd)

coprimepair()