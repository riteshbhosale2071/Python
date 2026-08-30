import math

def pythagoreantriple():
    limit = int(input("Enter the maximum value for the hypotenuse: "))

    if limit < 5:
        print("Enter a value of at least 5.")
        return

    print("Pythagorean Triples:")

    found = False

    for a in range(1, limit):
        for b in range(a + 1, limit):
            c = math.sqrt(a ** 2 + b ** 2)

            if c.is_integer() and c <= limit:
                print(f"({a}, {b}, {int(c)})")
                found = True

    if not found:
        print("No Pythagorean triples found.")

pythagoreantriple()