def smallestpythagoreantriple():
    limit = int(input("Enter the maximum value to search: "))

    if limit < 5:
        print("Enter a value of at least 5.")
        return

    found = False

    for c in range(5, limit + 1):
        for a in range(1, c):
            for b in range(a + 1, c):
                if a * a + b * b == c * c:
                    print("Smallest Pythagorean Triple:")
                    print(f"({a}, {b}, {c})")
                    found = True
                    return

    if not found:
        print("No Pythagorean Triple found in the given range.")

smallestpythagoreantriple()