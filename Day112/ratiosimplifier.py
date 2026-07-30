def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ratiosimplifier():
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    gcd = find_gcd(first, second)

    print("Simplified Ratio:", first // gcd, ":", second // gcd)

ratiosimplifier()