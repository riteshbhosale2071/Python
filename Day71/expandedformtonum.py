def conv():
    expanded = input("Enter expanded form (e.g., 500 + 80 + 3): ")

    parts = expanded.split("+")

    total = 0

    for part in parts:
        total += int(part.strip())

    print("Number =", total)

conv()