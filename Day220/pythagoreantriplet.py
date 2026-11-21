import math

def pythagoreantriplet():
    print("Pythagorean Triplet :")

    limit = int(input("Enter the maximum value for triplet numbers: "))

    if limit < 3:
        print("Enter a limit greater than or equal to 3.")
        return

    print("\nGenerated Pythagorean Triplets:")

    count = 0

    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            c = math.isqrt(a ** 2 + b ** 2)

            if c <= limit and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                count += 1

    if count == 0:
        print("No Pythagorean triplets found.")

    print("\nTotal Triplets Generated:", count)

pythagoreantriplet()