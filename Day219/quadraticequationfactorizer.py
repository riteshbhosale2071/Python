import math

def quadraticequationfactorizer():
    print("Quadratic Equation Factorizer")
    print("Standard Form: ax² + bx + c = 0")

    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    if a == 0:
        print("Not a quadratic equation.")
        return

    discriminant = b ** 2 - 4 * a * c

    print("\nQuadratic Equation: {}x² + {}x + {} = 0".format(a, b, c))

    if discriminant < 0:
        print("The equation cannot be factorized into real linear factors.")
        return

    root = math.isqrt(discriminant)

    if root ** 2 != discriminant:
        print("The equation does not have rational roots.")
        print("Roots are irrational or real surds.")
        return

    factors = []
    for i in range(1, abs(a) + 1):
        if a % i == 0:
            factors.append(i)
            factors.append(-i)

    found = False

    for p in factors:
        if a % p == 0:
            q = a // p
            for r in range(-abs(c), abs(c) + 1):
                if r * (c // r) == c if r != 0 and c % r == 0 else False:
                    s = c // r
                    if p * s + q * r == b:
                        print("Factorized Form: ({}x + {})({}x + {}) = 0".format(p, r, q, s))
                        found = True
                        break
            if found:
                break

    if not found:
        print("The equation has no integer factorization.")

quadraticequationfactorizer()