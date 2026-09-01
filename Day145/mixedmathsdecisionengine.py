import math

def mixedmathsdecisionengine():
    print("Mixed Maths Decision Engine :")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Perfect Number")
    print("4. Check Perfect Square")
    print("5. Calculate HCF")
    print("6. Calculate LCM")
    print("7. Check Pythagorean Triple")
    print("8. Check Triangle Validity")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter a number: "))

        if n % 2 == 0:
            print("The number is Even.")
        else:
            print("The number is Odd.")

    elif choice == 2:
        n = int(input("Enter a number: "))

        if n < 2:
            print("The number is Not Prime.")
            return

        prime = True

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("The number is Prime.")
        else:
            print("The number is Not Prime.")

    elif choice == 3:
        n = int(input("Enter a number: "))

        if n <= 0:
            print("Enter a positive number.")
            return

        factor_sum = 0

        for i in range(1, n):
            if n % i == 0:
                factor_sum += i

        if factor_sum == n:
            print("The number is a Perfect Number.")
        else:
            print("The number is Not a Perfect Number.")

    elif choice == 4:
        n = int(input("Enter a number: "))

        if n < 0:
            print("Negative numbers cannot be perfect squares.")
            return

        root = math.isqrt(n)

        if root * root == n:
            print("The number is a Perfect Square.")
        else:
            print("The number is Not a Perfect Square.")

    elif choice == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("HCF:", math.gcd(a, b))

    elif choice == 6:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if a == 0 or b == 0:
            print("LCM is 0.")
        else:
            lcm = abs(a * b) // math.gcd(a, b)
            print("LCM:", lcm)

    elif choice == 7:
        a = int(input("Enter first side: "))
        b = int(input("Enter second side: "))
        c = int(input("Enter third side: "))

        sides = sorted([a, b, c])

        if sides[0] <= 0:
            print("Sides must be positive.")
        elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            print("The numbers form a Pythagorean Triple.")
        else:
            print("The numbers do not form a Pythagorean Triple.")

    elif choice == 8:
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Invalid triangle.")
        elif a + b > c and a + c > b and b + c > a:
            print("Triangle Construction is Possible.")
        else:
            print("Triangle Construction is Not Possible.")

    else:
        print("Invalid choice.")

mixedmathsdecisionengine()